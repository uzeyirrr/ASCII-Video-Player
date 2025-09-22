#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test video oluşturucu - ASCII player'ı test etmek için
"""

import cv2
import numpy as np

def create_test_video():
    """Basit bir test video dosyası oluştur"""
    
    # Video ayarları
    width, height = 320, 240
    fps = 10
    duration = 3  # 3 saniye
    total_frames = fps * duration
    
    # Video writer oluştur
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('test_video.mp4', fourcc, fps, (width, height))
    
    print("🎬 Test video oluşturuluyor...")
    
    for frame_num in range(total_frames):
        # Her frame için farklı bir görüntü oluştur
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        
        # Animasyonlu daire
        center_x = int(width/2 + 50 * np.sin(frame_num * 0.2))
        center_y = int(height/2 + 30 * np.cos(frame_num * 0.2))
        radius = 20 + int(10 * np.sin(frame_num * 0.3))
        
        # Daire çiz
        cv2.circle(frame, (center_x, center_y), radius, (255, 255, 255), -1)
        
        # Frame numarası yaz
        cv2.putText(frame, f"Frame: {frame_num+1}", (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Zaman yaz
        time_text = f"Time: {frame_num/fps:.1f}s"
        cv2.putText(frame, time_text, (10, 60), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Video'ya frame ekle
        out.write(frame)
        
        # İlerleme göster
        if frame_num % 10 == 0:
            progress = (frame_num + 1) / total_frames * 100
            print(f"İlerleme: {progress:.1f}%")
    
    # Video'yu kapat
    out.release()
    print("✅ Test video oluşturuldu: test_video.mp4")
    print("🚀 Şimdi şu komutu çalıştırın:")
    print("   python ascii_video_player.py test_video.mp4")

if __name__ == "__main__":
    create_test_video()
