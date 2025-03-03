#!/bin/sh

export $(grep -v '^#' .env | xargs)

DB_HOST=$PG_HOST

echo "Waiting for database to be ready..."
while ! nc -z $DB_HOST 5432; do
  sleep 1

done

echo "Database is ready!"
# poetry run alembic upgrade head
exec poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000