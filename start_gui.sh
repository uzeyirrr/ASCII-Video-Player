#!/bin/bash

# ASCII Video Player GUI Başlatıcı
# Linux/Mac için bash script

echo ""
echo "==============================================="
echo "🎥 ASCII Video Player GUI Başlatılıyor..."
echo "==============================================="
echo ""

# Renk kodları
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Python'un yüklü olup olmadığını kontrol et
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo -e "${RED}❌ Python bulunamadı! Lütfen Python'u yükleyin.${NC}"
        echo -e "${BLUE}💡 Ubuntu/Debian: sudo apt install python3 python3-pip${NC}"
        echo -e "${BLUE}💡 macOS: brew install python3${NC}"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

echo -e "${GREEN}✅ Python bulundu!${NC}"
echo ""

# Gerekli kütüphaneleri kontrol et
echo -e "${YELLOW}📦 Kütüphaneler kontrol ediliyor...${NC}"
$PYTHON_CMD -c "import cv2, numpy, PIL, colorama" 2>/dev/null
if [ $? -ne 0 ]; then
    echo -e "${YELLOW}⚠️  Bazı kütüphaneler eksik. Yükleniyor...${NC}"
    echo ""
    
    # pip3 veya pip kullan
    if command -v pip3 &> /dev/null; then
        PIP_CMD="pip3"
    else
        PIP_CMD="pip"
    fi
    
    $PIP_CMD install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo -e "${RED}❌ Kütüphane yükleme başarısız!${NC}"
        echo -e "${BLUE}💡 Manuel olarak şu komutu deneyin:${NC}"
        echo "   $PIP_CMD install opencv-python pillow colorama numpy"
        exit 1
    fi
    echo -e "${GREEN}✅ Kütüphaneler yüklendi!${NC}"
else
    echo -e "${GREEN}✅ Tüm kütüphaneler mevcut!${NC}"
fi

echo ""
echo -e "${BLUE}🚀 GUI başlatılıyor...${NC}"
echo ""

# GUI'yi başlat
$PYTHON_CMD video_player_gui.py

# Hata durumunda bilgi ver
if [ $? -ne 0 ]; then
    echo ""
    echo -e "${RED}❌ GUI başlatılamadı!${NC}"
    echo -e "${BLUE}💡 Manuel olarak şu komutu deneyin:${NC}"
    echo "   $PYTHON_CMD video_player_gui.py"
    echo ""
    read -p "Devam etmek için Enter'a basın..."
fi
