@echo off

:: Exit early if any commands fail
setlocal EnableDelayedExpansion

:: Run Python script with pipenv
pipenv run python -u -m app.main %*

endlocal
