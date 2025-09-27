@echo off
echo Verificando instalacion de Python...

where python >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python no esta instalado. Por favor instale Python desde:
    echo https://www.python.org/downloads/
    echo Asegurese de marcar "Add Python to PATH" durante la instalacion
    pause
    exit /b 1
)

echo Instalando dependencias...
python -m pip install -r requirements.txt

echo Iniciando servidor...
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
pause
