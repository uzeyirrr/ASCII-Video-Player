#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dikey test video oluşturucu
"""

import cv2
import numpy as np

def create_vertical_test_video():
    """Dikey test video dosyası oluştur - daha uzun ve detaylı"""
    
    # Video ayarları (dikey)
    width, height = 200, 400  # Daha uzun dikey format
    fps = 8
    duration = 5  # 5 saniye
    total_frames = fps * duration
    
    # Video writer oluştur
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('test_vertical_video.mp4', fourcc, fps, (width, height))
    
    print("🎬 Dikey test video oluşturuluyor...")
    
    for frame_num in range(total_frames):
        # Her frame için farklı bir görüntü oluştur
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        
        # Arka plan gradyanı
        for y in range(height):
            intensity = int(50 + (y / height) * 100)
            frame[y, :] = [intensity//3, intensity//2, intensity]
        
        # Animasyonlu daire (dikey hareket)
        center_x = int(width/2)
        center_y = int(height/2 + 80 * np.sin(frame_num * 0.15))
        radius = 25 + int(15 * np.sin(frame_num * 0.2))
        
        # Daire çiz (beyaz)
        cv2.circle(frame, (center_x, center_y), radius, (255, 255, 255), -1)
        cv2.circle(frame, (center_x, center_y), radius, (200, 200, 200), 2)
        
        # İç daire
        inner_radius = radius // 2
        cv2.circle(frame, (center_x, center_y), inner_radius, (100, 100, 100), -1)
        
        # Frame numarası yaz (üstte)
        cv2.putText(frame, f"Frame: {frame_num+1}", (10, 25), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        # Zaman yaz (altta)
        time_text = f"Time: {frame_num/fps:.1f}s"
        cv2.putText(frame, time_text, (10, height-15), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        # Dikey çizgiler ekle (kenarlar)
        for i in range(0, width, 25):
            cv2.line(frame, (i, 0), (i, height), (150, 150, 150), 1)
        
        # Yatay çizgiler ekle
        for i in range(0, height, 50):
            cv2.line(frame, (0, i), (width, i), (120, 120, 120), 1)
        
        # Köşelerde küçük kareler
        cv2.rectangle(frame, (10, 10), (30, 30), (255, 255, 255), 2)
        cv2.rectangle(frame, (width-30, 10), (width-10, 30), (255, 255, 255), 2)
        cv2.rectangle(frame, (10, height-30), (30, height-10), (255, 255, 255), 2)
        cv2.rectangle(frame, (width-30, height-30), (width-10, height-10), (255, 255, 255), 2)
        
        # Video'ya frame ekle
        out.write(frame)
        
        # İlerleme göster
        if frame_num % 8 == 0:
            progress = (frame_num + 1) / total_frames * 100
            print(f"İlerleme: {progress:.1f}%")
    
    # Video'yu kapat
    out.release()
    print("✅ Dikey test video oluşturuldu: test_vertical_video.mp4")
    print("🚀 Şimdi şu komutu çalıştırın:")
    print("   python ascii_video_player.py test_vertical_video.mp4 -w 40")

if __name__ == "__main__":
    create_vertical_test_video()
