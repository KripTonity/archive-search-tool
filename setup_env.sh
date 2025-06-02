#!/bin/bash

echo "📦 Creating virtual environment..."
python3 -m venv venv

echo "✅ Virtual environment created."
echo "📥 Installing dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ All dependencies installed."
echo "🎉 Setup complete. To activate the environment, run:"
echo "source venv/bin/activate"
