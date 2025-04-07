@echo off
echo 🔧 Setting up chat2md local development environment...

REM Create virtual environment
python -m venv .venv
call .venv\Scripts\activate

REM Upgrade pip and install package
python -m pip install --upgrade pip
pip install .

REM Initialize git and set remote
git init
set /p repo_url="Enter your GitHub repo URL (e.g. https://github.com/rgoshen/chat2md.git): "
git remote add origin %repo_url%

git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main

echo ✅ Setup complete. chat2md installed in virtual environment and pushed to GitHub.
echo 💡 To activate your environment next time, run: call .venv\Scripts\activate
pause
