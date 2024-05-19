@echo off
pip install -r requirements.txt || exit /b 1
cls
python "%~dp0collector.py"  || exit /b 1
pause