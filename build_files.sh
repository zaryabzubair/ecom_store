echo "Virtual environment setup..."
python3.9 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Building project packages..."
python3.9 -m pip install -r requirements.txt

echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput --clear
