@echo off
echo === Iniciando sistema de panaderia ===

echo 1. Verificando Python...
python --version
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python no esta instalado
    pause
    exit /b 1
)

echo 2. Instalando dependencias...
python -m pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv

echo 3. Iniciando servidor...
echo Para detener el servidor presione Ctrl+C
echo Luego responda 'S' para terminar el batch job

python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

echo Servidor detenido
pause
