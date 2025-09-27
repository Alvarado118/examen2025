```bash
@echo off
SET HOST=127.0.0.1
SET PORT=8000

echo Verificando dependencias...
python -m pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv

echo Iniciando servidor en http://%HOST%:%PORT%
python -m uvicorn app.main:app --reload --host %HOST% --port %PORT%
pause
```
# Instalar dependencias
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv

# Navegar al directorio del proyecto
cd c:\Users\ander\Desktop\panaderia-api

# Ejecutar el servidor
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000# Ejecutar el script
.\run.sh