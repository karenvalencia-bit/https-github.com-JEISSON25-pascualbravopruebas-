FROM wordpress:6.4-php8.2-apache

RUN apt-get update \
 && apt-get install -y less curl \
 && curl -sSL https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar \
    -o /usr/local/bin/wp \
 && chmod +x /usr/local/bin/wp

WORKDIR /var/www/html
