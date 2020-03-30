FROM nginx:latest

WORKDIR /app

# Remove default site
RUN rm /etc/nginx/sites-enabled/default.conf

# Create certificate directory
RUN mkdir -p /var/www/_letsencrypt
RUN chown www-data /var/www/_letsencrypt

# Load Nginx configs
COPY nginx.conf /etc/nginx/nginx.conf
COPY nginx-site.conf /etc/nginx/sites-enabled/nginx.conf

CMD /app/entry.sh
