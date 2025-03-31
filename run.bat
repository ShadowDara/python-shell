@echo off

:: Exit early if any commands fail
setlocal EnableDelayedExpansion

:: Run Python script with pipenv
rem pipenv run python -u -m app.main %*
python app/main.py

endlocal
