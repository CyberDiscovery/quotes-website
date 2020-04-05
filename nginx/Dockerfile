FROM nginx:latest

WORKDIR /app

#RUN apt update
#RUN apt install gpg -y
#RUN echo "deb http://ppa.launchpad.net/mcasadevall/certbot0.25.1/ubuntu bionic main\ndeb-src http://ppa.launchpad.net/mcasadevall/certbot0.25.1/ubuntu bionic main" > /etc/apt/sources.list
#RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6A21F735BDE103953B400EEB024E42392D8C83B2
#RUN apt update
#RUN apt install python3 certbot python3-certbot-nginx -y
#RUN apt clean

# Remove default site
RUN rm /etc/nginx/conf.d/default.conf

# Create certificate directory
RUN mkdir -p /var/www/_letsencrypt
RUN chown www-data /var/www/_letsencrypt

# Load Nginx configs
COPY nginx.conf /etc/nginx/nginx.conf
COPY nginx-site.conf /etc/nginx/conf.d/nginx.conf
COPY entry.sh entry.sh

CMD sh /app/entry.sh
