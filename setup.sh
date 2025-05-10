#!/bin/bash

# Setup script for Yves Programmeur Quiz App

echo "Setting up Yves Programmeur Quiz App..."

# Create virtual environment for backend
echo "Creating virtual environment for backend..."
cd backend
python3 -m venv venv
source venv/bin/activate

# Install backend dependencies
echo "Installing backend dependencies..."
pip install -r requirements.txt

# Run migrations
echo "Running database migrations..."
python3 manage.py makemigrations users
python3 manage.py makemigrations quizzes
python3 manage.py migrate

# Create superuser
echo "Creating superuser..."
python3 manage.py createsuperuser

# Deactivate virtual environment
deactivate

# Install frontend dependencies
echo "Installing frontend dependencies..."
cd ../frontend
npm install

echo "Setup complete!"
echo "To run the backend server: cd backend && source venv/bin/activate && python manage.py runserver"
echo "To run the frontend server: cd frontend && npm start"
