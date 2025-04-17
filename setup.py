@echo off
setlocal
echo 🔧 Setting up chat2md (Windows)...

REM Create virtual environment
python -m venv .venv

REM Activate virtual environment
call .venv\Scripts\activate

REM Install dependencies
python -m pip install --upgrade pip
pip install -e .[dev]

REM Optional: Initialize Git repo
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

echo ✅ chat2md is ready. To activate later, run: call .venv\Scripts\activate
endlocal
