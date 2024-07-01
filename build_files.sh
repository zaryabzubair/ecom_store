
echo "Building project packages..."
pip3.9 install -r requirements.txt

echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput
