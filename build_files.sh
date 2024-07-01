#!/bin/bash
echo "Building project packages..."
python3.9 -m pip install --upgrade pip
python3.9 pip install -r requirements.txt

echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput
