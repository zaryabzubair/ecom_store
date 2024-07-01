#!/bin/bash
echo "Building project packages..."
pip install -r requirements.txt

echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput
