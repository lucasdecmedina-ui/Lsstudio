@echo off
chcp 65001 >nul
cd /d "%~dp0"
title LS Studio Santos - Previa local
python iniciar-preview.py
if errorlevel 1 pause
