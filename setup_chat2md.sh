#!/bin/bash
set -e

echo "Setting up chat2md (macOS/Linux)..."

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install project and dev tools
pip install --upgrade pip
pip install -e .[dev]

# Optionally set up VSCode Python path
mkdir -p .vscode
echo -e '{\n  "python.pythonPath": ".venv/bin/python"\n}' >.vscode/settings.json

# Optional: Initialize Git
if [ ! -d ".git" ]; then
  git init
  read -p "Enter your GitHub repo URL (or leave blank to skip): " repo_url
  if [ -n "$repo_url" ]; then
    git remote add origin "$repo_url"
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git push -u origin main
  fi
fi

echo "chat2md setup complete."
echo "To activate your environment later, run: source .venv/bin/activate"
