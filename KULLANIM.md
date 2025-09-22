# 🎥 ASCII Video Player - Kullanım Kılavuzu

## 📋 Kurulum

1. **Gerekli kütüphaneleri yükleyin:**
```bash
pip install -r requirements.txt
```

## 🚀 Kullanım

### 🖥️ GUI Arayüzü (Önerilen)

#### Windows
```bash
start_gui.bat
```

#### Linux/Mac
```bash
./start_gui.sh
```

#### Manuel Başlatma
```bash
python video_player_gui.py
```

**Özellikler:**
- Modern grafik arayüz
- Video dosyası seçimi
- Ayarları kolayca değiştirme
- Gerçek zamanlı önizleme
- Otomatik kütüphane kontrolü

### 💻 Komut Satırı Kullanımı

#### Temel Kullanım
```bash
python ascii_video_player.py video_dosyasi.mp4
```

#### Gelişmiş Seçenekler
```bash
# Genişlik ayarı (varsayılan: 80)
python ascii_video_player.py video.mp4 -w 120

# FPS ayarı (varsayılan: 30)
python ascii_video_player.py video.mp4 -f 10

# Video bilgilerini göster
python ascii_video_player.py video.mp4 -i

# Her iki seçenek birlikte
python ascii_video_player.py video.mp4 -w 100 -f 15
```

## 🖥️ GUI Özellikleri

### 📁 Video Seçimi
- **Gözat** butonu ile video dosyası seçimi
- Desteklenen formatlar: MP4, AVI, MOV, MKV, WMV, FLV
- Seçilen dosya yolu otomatik gösterimi

### ⚙️ Ayarlar
- **ASCII Genişlik**: 40-120 arası kaydırma çubuğu
- **FPS**: 5-60 arası kaydırma çubuğu
- Gerçek zamanlı değer gösterimi

### 🎮 Butonlar
- **📊 Video Bilgileri**: Metadata gösterimi
- **▶️ ASCII Oynat**: Terminal'de oynatma
- **🖥️ Terminal'de Aç**: Yeni terminal penceresi

### 📋 Çıktı Alanı
- Terminal benzeri yeşil metin
- Gerçek zamanlı log mesajları
- Kaydırma çubuğu

## ⚙️ Komut Satırı Parametreleri

- `video_path`: Oynatılacak video dosyasının yolu (gerekli)
- `-w, --width`: ASCII çıktı genişliği (varsayılan: 80)
- `-f, --fps`: Oynatma FPS değeri (varsayılan: 30)
- `-i, --info`: Sadece video bilgilerini göster

## 🎯 Öneriler

- **Genişlik**: 60-120 arası değerler optimal
- **FPS**: 10-30 arası değerler önerilir
- **Video formatları**: MP4, AVI, MOV desteklenir
- **Video boyutu**: Küçük dosyalar daha iyi performans verir

## ⌨️ Kontroller

- `Ctrl+C`: Videoyu durdur
- Video otomatik olarak sonuna kadar oynar

## 🎨 ASCII Karakterleri

Kullanılan karakterler (koyudan açığa):
```
 .:-=+*#%@
```

## 🔧 Sorun Giderme

- **Video açılmıyor**: Dosya yolunu kontrol edin
- **Yavaş oynatma**: FPS değerini düşürün (`-f 5`)
- **ASCII çok büyük**: Genişlik değerini azaltın (`-w 60`)
