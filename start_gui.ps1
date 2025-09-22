# ASCII Video Player GUI Başlatıcı
# PowerShell script

Write-Host ""
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "🎥 ASCII Video Player GUI Başlatılıyor..." -ForegroundColor Yellow
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

# Python'un yüklü olup olmadığını kontrol et
try {
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "Python bulunamadı"
    }
    Write-Host "✅ Python bulundu: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python bulunamadı! Lütfen Python'u yükleyin." -ForegroundColor Red
    Write-Host "💡 https://python.org adresinden indirebilirsiniz." -ForegroundColor Blue
    Read-Host "Devam etmek için Enter'a basın"
    exit 1
}

Write-Host ""

# Gerekli kütüphaneleri kontrol et
Write-Host "📦 Kütüphaneler kontrol ediliyor..." -ForegroundColor Yellow
try {
    python -c "import cv2, numpy, PIL, colorama" 2>$null
    if ($LASTEXITCODE -ne 0) {
        throw "Kütüphaneler eksik"
    }
    Write-Host "✅ Tüm kütüphaneler mevcut!" -ForegroundColor Green
} catch {
    Write-Host "⚠️  Bazı kütüphaneler eksik. Yükleniyor..." -ForegroundColor Yellow
    Write-Host ""
    
    pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Kütüphane yükleme başarısız!" -ForegroundColor Red
        Read-Host "Devam etmek için Enter'a basın"
        exit 1
    }
    Write-Host "✅ Kütüphaneler yüklendi!" -ForegroundColor Green
}

Write-Host ""
Write-Host "🚀 GUI başlatılıyor..." -ForegroundColor Blue
Write-Host ""

# GUI'yi başlat
python video_player_gui.py

# Hata durumunda bilgi ver
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "❌ GUI başlatılamadı!" -ForegroundColor Red
    Write-Host "💡 Manuel olarak şu komutu deneyin:" -ForegroundColor Blue
    Write-Host "   python video_player_gui.py" -ForegroundColor White
    Write-Host ""
    Read-Host "Devam etmek için Enter'a basın"
}
