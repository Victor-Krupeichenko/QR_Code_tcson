@echo off

REM Путь к виртуальному окружению
set VENV_DIR=.venv

REM Активирую виртуальное окружение
call %VENV_DIR%\Scripts\activate.bat

echo [Start] Nuitka ONEFILE compilation started...

python -m nuitka ^
    --onefile ^
    --enable-plugin=pyside6 ^
    --windows-console-mode=disable ^
    --include-windows-runtime-dlls=yes ^
    --assume-yes-for-downloads ^
    --windows-icon-from-ico=start_icon_exe.ico ^
    --windows-company-name="LOEV TCSON" ^
    --windows-product-name="LOEV TCSON QRCode Generator" ^
    --windows-file-description="LOEV TCSON QRCode Generator" ^
    --windows-file-version="1.0.0" ^
    --windows-product-version="1.0.0" ^
    --output-dir="LOEV TCSON QRCode Generator" ^
    --output-filename="LOEV TCSON QRCode Generator.exe" ^
    --remove-output ^
    main.py

echo [Done] Nuitka ONEFILE compilation completed.
pause


