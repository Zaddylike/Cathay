@echo off
chcp 65001 >nul

echo ==============================
echo Cleaning __pycache__ folders...
echo ==============================

for /d /r %%d in (__pycache__) do (
    if exist "%%d" (
        echo Delete: %%d
        rmdir /s /q "%%d"

        if errorlevel 1 (
            echo Failed to delete: %%d
        )
    )
)

echo.
echo ==============================
echo Cleaning .pyc files...
echo ==============================

for /r %%f in (*.pyc) do (
    if exist "%%f" (
        echo Delete: %%f
        del /f /q "%%f"

        if errorlevel 1 (
            echo Failed to delete: %%f
        )
    )
)

echo.
echo ==============================
echo Clean completed.
echo ==============================

pause