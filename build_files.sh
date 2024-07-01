#!/bin/sh

echo "Building project packages..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput
