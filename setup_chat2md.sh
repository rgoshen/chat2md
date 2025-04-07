#!/bin/bash

# Exit on error
set -e

echo "🔧 Setting up chat2md local development environment..."

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install the chat2md package
pip install --upgrade pip
pip install .

# Initialize git and set remote
git init
read -p "Enter your GitHub repo URL (e.g. https://github.com/rgoshen/chat2md.git): " repo_url
git remote add origin "$repo_url"

# Add files and make initial commit
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main

echo "✅ Setup complete. chat2md installed in virtual environment and pushed to GitHub."
echo "💡 To activate your environment next time, run: source .venv/bin/activate"
