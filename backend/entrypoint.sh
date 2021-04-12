#!/bin/sh

echo "Waiting for mysql to start..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 2
done

echo "Mysql started"

exec "$@"