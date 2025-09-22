@echo off
title ASCII Video Player GUI
color 0A

echo.
echo  ===============================================
echo  🎥 ASCII Video Player GUI Başlatılıyor...
echo  ===============================================
echo.

REM Python'un yüklü olup olmadığını kontrol et
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python bulunamadı! Lütfen Python'u yükleyin.
    echo 💡 https://python.org adresinden indirebilirsiniz.
    pause
    exit /b 1
)

echo ✅ Python bulundu!
echo.

REM Gerekli kütüphaneleri kontrol et
echo 📦 Kütüphaneler kontrol ediliyor...
python -c "import cv2, numpy, PIL, colorama" >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Bazı kütüphaneler eksik. Yükleniyor...
    echo.
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ Kütüphane yükleme başarısız!
        pause
        exit /b 1
    )
    echo ✅ Kütüphaneler yüklendi!
) else (
    echo ✅ Tüm kütüphaneler mevcut!
)

echo.
echo 🚀 GUI başlatılıyor...
echo.

REM GUI'yi başlat
python video_player_gui.py

REM Hata durumunda bekle
if errorlevel 1 (
    echo.
    echo ❌ GUI başlatılamadı!
    echo 💡 Manuel olarak şu komutu deneyin:
    echo    python video_player_gui.py
    echo.
    pause
)
