@echo off
echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install Flask==3.0.0 scikit-learn==1.3.2 numpy==1.26.2

echo.
echo Setup complete!
echo.
echo To run the application:
echo 1. Activate venv: venv\Scripts\activate
echo 2. Run app: python app.py
echo.
pause
