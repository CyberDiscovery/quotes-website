#!/bin/bash

# Get certificate
sed -i -r 's/(listen .*443)/\1;#/g; s/(ssl_(certificate|certificate_key|trusted_certificate) )/#;#\1/g' /etc/nginx/conf.d/nginx.conf 
nginx -t && systemctl reload nginx 
certbot certonly --webroot -d quotes@cyberdiscoverycommunity.uk --email triggerhappymods@cyberdiscoverycommunity.uk -w /var/www/_letsencrypt -n --agree-tos --force-renewal
sed -i -r 's/#?;#//g' /etc/nginx/conf.d/nginx.conf
nginx -t && systemctl reload nginx 
echo -e '#!/bin/bash\nnginx -t && systemctl reload nginx' | sudo tee /etc/letsencrypt/renewal-hooks/post/nginx-reload.sh
sudo chmod a+x /etc/letsencrypt/renewal-hooks/post/nginx-reload.sh

# Complete Nginx setup
nginx -t && systemctl reload nginx
