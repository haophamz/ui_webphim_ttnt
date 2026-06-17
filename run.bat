@echo off
chcp 65001 >nul
echo ============================================
echo   N4 Episodes Module - Khoi dong server
echo ============================================
echo.

set PYTHONUTF8=1

if not exist "movie_app.db" (
    echo [1/2] Tao database va seed du lieu mau...
    .venv312\Scripts\python.exe seed_data.py
    echo.
) else (
    echo [INFO] Database da ton tai, bo qua buoc seed.
    echo.
)

echo [2/2] Khoi dong Flask server tai http://127.0.0.1:5000
echo Nhan Ctrl+C de dung server.
echo.
.venv312\Scripts\python.exe app.py
