@echo off
echo === Instalacion Sistema Panaderia ===

REM Verificar si Python esta instalado via Microsoft Store
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Python no esta instalado. Siga estos pasos:
    echo.
    echo 1. Descargar Python desde: https://www.python.org/downloads/
    echo 2. IMPORTANTE: Marcar "Add Python to PATH" durante la instalacion
    echo 3. Reiniciar la computadora
    echo 4. Volver a ejecutar este script
    echo.
    echo Presione cualquier tecla para abrir la pagina de descarga...
    pause >nul
    start https://www.python.org/downloads/
    exit /b 1
)

echo Python encontrado, instalando dependencias...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo.
echo Instalacion completada. 
echo Para iniciar el servidor ejecute: run.bat
pause
