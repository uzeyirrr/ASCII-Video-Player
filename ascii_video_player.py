#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ASCII Video Player
Video dosyalarını terminalde ASCII formatında oynatır
"""

import cv2
import numpy as np
import time
import os
import sys
from PIL import Image
import argparse
from colorama import init, Fore, Style

# Colorama'yı başlat
init()

class ASCIIVideoPlayer:
    def __init__(self, width=120, fps=30):
        self.width = width
        self.fps = fps
        # ASCII karakterleri (koyudan açığa) - yüksek çözünürlük
        self.ascii_chars = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
        # Flicker önleme için
        self.last_frame = None
        self.terminal_width, self.terminal_height = self.get_terminal_size()
        # Double buffering için
        self.frame_buffer = []
        self.buffer_size = 3
        
    def resize_frame(self, frame):
        """Frame'i belirtilen genişliğe göre yeniden boyutlandır"""
        height = int(frame.shape[0] * self.width / frame.shape[1])
        return cv2.resize(frame, (self.width, height))
    
    def frame_to_ascii(self, frame):
        """Frame'i ASCII karakterlere dönüştür - yüksek çözünürlük"""
        # Gri tonlamaya çevir
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Kontrast artırma (CLAHE - Contrast Limited Adaptive Histogram Equalization)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        gray = clahe.apply(gray)
        
        # Gaussian blur ile yumuşatma (detayları korur)
        gray = cv2.GaussianBlur(gray, (1, 1), 0)
        
        # ASCII karakterlere dönüştür
        ascii_lines = []
        for row in gray:
            line = ""
            for pixel in row:
                # Pixel değerini ASCII karakter indeksine dönüştür
                # Daha hassas mapping için float kullan
                char_index = int((pixel / 255.0) * (len(self.ascii_chars) - 1))
                # Sınırları kontrol et
                char_index = max(0, min(char_index, len(self.ascii_chars) - 1))
                line += self.ascii_chars[char_index]
            ascii_lines.append(line)
        
        return ascii_lines
    
    def get_terminal_size(self):
        """Terminal boyutunu al"""
        try:
            import shutil
            size = shutil.get_terminal_size()
            return size.columns, size.lines
        except:
            return 80, 24  # Varsayılan boyut
    
    def center_ascii_frame(self, ascii_lines):
        """ASCII frame'i terminal'de ortala - dikey videolar için optimize edilmiş"""
        terminal_width, terminal_height = self.get_terminal_size()
        
        if not ascii_lines:
            return ""
        
        # ASCII frame boyutları
        ascii_width = len(ascii_lines[0]) if ascii_lines else 0
        ascii_height = len(ascii_lines)
        
        # Dikey video tespiti (yükseklik > genişlik)
        is_vertical = ascii_height > ascii_width
        
        # Yatay ortalama
        horizontal_padding = max(0, (terminal_width - ascii_width) // 2)
        
        # Dikey ortalama - dikey videolar için daha fazla üst boşluk
        if is_vertical:
            # Dikey videolar için: terminal'in üst 1/3'ü boş bırak
            vertical_padding = max(5, terminal_height // 3)
            # Maksimum boşluk sınırı
            vertical_padding = min(vertical_padding, 15)
        else:
            # Yatay videolar için normal ortalama
            vertical_padding = max(0, (terminal_height - ascii_height - 10) // 2)
        
        # Ortalanmış frame oluştur
        centered_lines = []
        
        # Üst boşluk ekle
        for _ in range(vertical_padding):
            centered_lines.append("")
        
        # ASCII satırlarını ortala
        for line in ascii_lines:
            centered_line = " " * horizontal_padding + line
            centered_lines.append(centered_line)
        
        # Dikey videolar için alt boşluk da ekle
        if is_vertical:
            bottom_padding = max(3, (terminal_height - len(centered_lines) - 10) // 2)
            for _ in range(bottom_padding):
                centered_lines.append("")
        
        return "\n".join(centered_lines)
    
    def clear_screen(self):
        """Terminal ekranını temizle - flicker önleme ile"""
        # ANSI escape kodları ile ekranı temizle (daha hızlı)
        print('\033[2J\033[H', end='')
        # Alternatif: os.system('cls' if os.name == 'nt' else 'clear')
    
    def update_frame_smooth(self, ascii_lines, frame_info):
        """Flicker önleme ile frame güncelle - optimize edilmiş"""
        # Terminal boyutunu güncelle
        self.terminal_width, self.terminal_height = self.get_terminal_size()
        
        # Ortalanmış frame oluştur
        centered_frame = self.center_ascii_frame(ascii_lines)
        
        # Başlık bilgilerini hazırla
        header = f"{Fore.CYAN}🎥 ASCII Video Player{Style.RESET_ALL}\n"
        header += f"{Fore.YELLOW}{frame_info}{Style.RESET_ALL}\n"
        header += "-" * 50 + "\n"
        
        # Tam frame'i oluştur
        full_frame = header + centered_frame
        
        # İlk frame ise ekranı temizle
        if self.last_frame is None:
            self.clear_screen()
        
        # Cursor'u başa al ve frame'i yazdır
        print('\033[H', end='')  # Cursor'u başa al
        print(full_frame, end='', flush=True)
        
        # Son frame'i kaydet
        self.last_frame = full_frame
    
    def get_video_info(self, video_path):
        """Video metadata bilgilerini al"""
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            return None
        
        # Video bilgilerini al
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = total_frames / fps if fps > 0 else 0
        
        # Codec bilgisi
        fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
        codec = "".join([chr((fourcc >> 8 * i) & 0xFF) for i in range(4)])
        
        cap.release()
        
        return {
            'width': width,
            'height': height,
            'fps': fps,
            'total_frames': total_frames,
            'duration': duration,
            'codec': codec
        }

    def load_video_frames(self, video_path):
        """Video'yu belleğe yükle ve ASCII'ye dönüştür"""
        print(f"🎬 Video yükleniyor ve işleniyor...")
        
        # Video bilgilerini al
        video_info = self.get_video_info(video_path)
        if not video_info:
            print(f"❌ Video açılamadı: {video_path}")
            return []
        
        # Video bilgilerini göster
        print(f"📹 Orijinal çözünürlük: {video_info['width']}x{video_info['height']}")
        print(f"🎯 Orijinal FPS: {video_info['fps']:.2f}")
        print(f"⏱️  Süre: {video_info['duration']:.1f} saniye")
        print(f"🎬 Toplam frame: {video_info['total_frames']}")
        print(f"💾 Codec: {video_info['codec']}")
        print(f"📏 ASCII genişlik: {self.width}")
        print(f"🎮 Oynatma FPS: {self.fps}")
        print("-" * 50)
        
        cap = cv2.VideoCapture(video_path)
        ascii_frames = []
        
        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Frame'i yeniden boyutlandır
            resized_frame = self.resize_frame(frame)
            
            # ASCII'ye dönüştür
            ascii_lines = self.frame_to_ascii(resized_frame)
            ascii_frames.append(ascii_lines)
            
            frame_count += 1
            if frame_count % 10 == 0:
                progress = (frame_count / video_info['total_frames']) * 100
                print(f"📊 İşleniyor: {progress:.1f}% ({frame_count}/{video_info['total_frames']})")
        
        cap.release()
        print(f"✅ {len(ascii_frames)} frame yüklendi!")
        return ascii_frames

    def play_video(self, video_path):
        """Video dosyasını ASCII formatında oynat"""
        if not os.path.exists(video_path):
            print(f"❌ Video dosyası bulunamadı: {video_path}")
            return
        
        # Video'yu belleğe yükle
        ascii_frames = self.load_video_frames(video_path)
        if not ascii_frames:
            return
        
        total_frames = len(ascii_frames)
        frame_delay = 1.0 / self.fps
        
        print(f"🎯 FPS: {self.fps}")
        print(f"📏 Genişlik: {self.width}")
        print(f"⏱️  Beklenen süre: {total_frames / self.fps:.1f} saniye")
        print(f"🚀 Oynatma başlıyor...")
        print("\n" + "="*50)
        
        time.sleep(1)  # Kısa bekleme
        
        try:
            for i, ascii_lines in enumerate(ascii_frames):
                # Frame bilgilerini hazırla
                frame_info = f"Frame: {i + 1}/{total_frames}"
                
                # Flicker önleme ile frame güncelle
                self.update_frame_smooth(ascii_lines, frame_info)
                
                # FPS'e göre bekle
                time.sleep(frame_delay)
                
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}⏹️  Video durduruldu{Style.RESET_ALL}")
        
        print(f"{Fore.GREEN}✅ Video oynatma tamamlandı{Style.RESET_ALL}")

def main():
    parser = argparse.ArgumentParser(description='ASCII Video Player')
    parser.add_argument('video_path', help='Oynatılacak video dosyasının yolu')
    parser.add_argument('-w', '--width', type=int, default=120, 
                       help='ASCII çıktı genişliği (varsayılan: 120)')
    parser.add_argument('-f', '--fps', type=float, default=30,
                       help='Oynatma FPS değeri (varsayılan: 30)')
    parser.add_argument('-i', '--info', action='store_true',
                       help='Sadece video bilgilerini göster (oynatma)')
    
    args = parser.parse_args()
    
    # ASCII Video Player'ı oluştur
    player = ASCIIVideoPlayer(width=args.width, fps=args.fps)
    
    if args.info:
        # Sadece video bilgilerini göster
        video_info = player.get_video_info(args.video_path)
        if video_info:
            print(f"{Fore.CYAN}📹 Video Bilgileri{Style.RESET_ALL}")
            print(f"📁 Dosya: {args.video_path}")
            print(f"📐 Çözünürlük: {video_info['width']}x{video_info['height']}")
            print(f"🎯 FPS: {video_info['fps']:.2f}")
            print(f"⏱️  Süre: {video_info['duration']:.1f} saniye")
            print(f"🎬 Toplam frame: {video_info['total_frames']}")
            print(f"💾 Codec: {video_info['codec']}")
            print(f"📏 ASCII genişlik: {args.width}")
            print(f"🎮 Oynatma FPS: {args.fps}")
        else:
            print(f"❌ Video açılamadı: {args.video_path}")
    else:
        # Video'yu oynat
        player.play_video(args.video_path)

if __name__ == "__main__":
    main()
