#!/bin/sh

if [ ! -d "/project/files" ]; then
    mkdir -p "/project/files"
fi

#chown -R www-data:www-data "./logs"
#chmod -R 777 "./logs"

exec "$@"
