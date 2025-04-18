@echo off
echo Setting up chat2md local development environment...

REM Create virtual environment
python -m venv .venv
call .venv\Scripts\activate

REM Upgrade pip and install with dev dependencies
python -m pip install --upgrade pip
pip install -e .[dev]

REM Optional: initialize git repo
if not exist ".git" (
    git init
    set /p repo_url=Enter your GitHub repo URL (or leave blank to skip):
    if not "%repo_url%"=="" (
        git remote add origin %repo_url%
        git add .
        git commit -m "Initial commit"
        git branch -M main
        git push -u origin main
    )
)

echo ✅ Setup complete.
echo 💡 To activate your environment later, run: call .venv\Scripts\activate
pause
