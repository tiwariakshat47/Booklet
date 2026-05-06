@echo off
echo Starting Booklet...

:: Activate conda environment
call C:\Users\aryan\miniconda3\Scripts\activate.bat booklet

:: Start FastAPI in the background
echo Starting FastAPI...
start "FastAPI" cmd /k "cd app && uvicorn main:app --reload"

:: Wait for API to be ready
echo Waiting for API to start...
timeout /t 3 /nobreak > nul

:: Start Streamlit and open browser
echo Starting Streamlit...
start "Streamlit" cmd /k "cd app && streamlit run streamlit_app.py"

:: Open browser
timeout /t 3 /nobreak > nul
start http://localhost:8501

echo Booklet is running!
echo - Streamlit UI: http://localhost:8501
echo - FastAPI docs: http://localhost:8000/docs