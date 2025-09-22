#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ASCII Video Player GUI
Video seçimi ve oynatma için grafik arayüz
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import subprocess
import os
from ascii_video_player import ASCIIVideoPlayer

class VideoPlayerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎥 ASCII Video Player - Modern Edition")
        self.root.geometry("800x700")
        self.root.configure(bg='#1a1a1a')
        self.root.resizable(True, True)
        
        # Modern renk paleti
        self.colors = {
            'bg_primary': '#1a1a1a',
            'bg_secondary': '#2d2d2d',
            'bg_tertiary': '#3a3a3a',
            'accent_blue': '#00d4ff',
            'accent_green': '#00ff88',
            'accent_purple': '#8b5cf6',
            'text_primary': '#ffffff',
            'text_secondary': '#b0b0b0',
            'text_accent': '#00d4ff',
            'border': '#404040',
            'success': '#00ff88',
            'warning': '#ffb800',
            'error': '#ff4757'
        } 
        
        # Stil ayarları
        self.setup_styles()
        
        # Ana frame
        self.main_frame = ttk.Frame(root, padding="30")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Başlık bölümü
        self.setup_header()
        
        # Video seçimi
        self.setup_video_selection()
        
        # Ayarlar
        self.setup_settings()
        
        # Butonlar
        self.setup_buttons()
        
        # Çıktı alanı
        self.setup_output_area()
        
        # Grid ağırlıkları
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        
        # Animasyon efekti
        self.animate_startup()
        
    def setup_styles(self):
        """Modern Tkinter stillerini ayarla"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Modern koyu tema
        style.configure('TLabel', 
                       background=self.colors['bg_primary'], 
                       foreground=self.colors['text_primary'],
                       font=('Segoe UI', 10))
        
        style.configure('TFrame', 
                       background=self.colors['bg_primary'])
        
        style.configure('Modern.TFrame',
                       background=self.colors['bg_secondary'],
                       relief='flat',
                       borderwidth=1)
        
        style.configure('Card.TFrame',
                       background=self.colors['bg_secondary'],
                       relief='flat',
                       borderwidth=0)
        
        # Modern butonlar
        style.configure('Modern.TButton',
                       background=self.colors['accent_blue'],
                       foreground=self.colors['text_primary'],
                       font=('Segoe UI', 10, 'bold'),
                       padding=(20, 12),
                       relief='flat',
                       borderwidth=0)
        
        style.map('Modern.TButton',
                 background=[('active', self.colors['accent_purple']),
                           ('pressed', self.colors['accent_green'])])
        
        # Başlık stili
        style.configure('Title.TLabel', 
                       font=('Segoe UI', 24, 'bold'),
                       foreground=self.colors['accent_blue'])
        
        # Alt başlık stili
        style.configure('Subtitle.TLabel',
                       font=('Segoe UI', 12),
                       foreground=self.colors['text_secondary'])
        
        # Giriş alanları
        style.configure('TEntry',
                       fieldbackground=self.colors['bg_tertiary'],
                       foreground=self.colors['text_primary'],
                       borderwidth=1,
                       relief='flat',
                       font=('Consolas', 10))
        
        # Scale (slider) stili - Tkinter uyumlu
        style.configure('TScale',
                       background=self.colors['bg_secondary'],
                       troughcolor=self.colors['bg_tertiary'],
                       borderwidth=0,
                       lightcolor=self.colors['accent_blue'],
                       darkcolor=self.colors['accent_blue'])
        
        # LabelFrame stili
        style.configure('Modern.TLabelframe',
                       background=self.colors['bg_secondary'],
                       foreground=self.colors['text_primary'],
                       font=('Segoe UI', 11, 'bold'),
                       borderwidth=1,
                       relief='flat')
        
        style.configure('Modern.TLabelframe.Label',
                       background=self.colors['bg_secondary'],
                       foreground=self.colors['accent_blue'],
                       font=('Segoe UI', 11, 'bold'))
    
    def setup_header(self):
        """Modern başlık bölümü"""
        header_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        header_frame.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 30))
        header_frame.columnconfigure(0, weight=1)
        
        # Ana başlık
        title_label = ttk.Label(
            header_frame, 
            text="🎥 ASCII Video Player", 
            style='Title.TLabel'
        )
        title_label.grid(row=0, column=0, pady=(20, 5))
        
        # Alt başlık
        subtitle_label = ttk.Label(
            header_frame,
            text="Modern Edition - Terminal'de Video Oynatma",
            style='Subtitle.TLabel'
        )
        subtitle_label.grid(row=1, column=0, pady=(0, 20))
        
        # Dekoratif çizgi
        separator = ttk.Frame(header_frame, height=2, style='Modern.TFrame')
        separator.grid(row=2, column=0, sticky=(tk.W, tk.E), padx=20, pady=(0, 20))
        
    def setup_video_selection(self):
        """Modern video seçimi bölümü"""
        # Video seçimi kartı
        video_frame = ttk.LabelFrame(self.main_frame, text="📁 Video Seçimi", style='Modern.TLabelframe', padding="20")
        video_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))
        video_frame.columnconfigure(1, weight=1)
        
        # Video dosyası seçimi
        ttk.Label(video_frame, text="📁 Video Dosyası:", font=('Segoe UI', 11, 'bold')).grid(
            row=0, column=0, sticky=tk.W, pady=(0, 15)
        )
        
        self.video_path_var = tk.StringVar()
        self.video_entry = ttk.Entry(
            video_frame, 
            textvariable=self.video_path_var,
            state='readonly',
            font=('Consolas', 10)
        )
        self.video_entry.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        self.browse_button = ttk.Button(
            video_frame,
            text="📂 Video Seç",
            style='Modern.TButton',
            command=self.browse_video
        )
        self.browse_button.grid(row=2, column=0, columnspan=2, pady=(0, 10))
        
        # Tooltip ekle
        self._create_tooltip(self.browse_button, "MP4, AVI, MOV, MKV ve diğer video formatlarını destekler")
        
    def setup_settings(self):
        """Modern ayarlar bölümü"""
        settings_frame = ttk.LabelFrame(self.main_frame, text="⚙️ Oynatma Ayarları", style='Modern.TLabelframe', padding="25")
        settings_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))
        settings_frame.columnconfigure(1, weight=1)
        
        # ASCII genişlik
        width_label = ttk.Label(settings_frame, text="📏 ASCII Genişlik:", font=('Segoe UI', 11, 'bold'))
        width_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 15))
        
        self.width_var = tk.IntVar(value=120)
        self.width_scale = ttk.Scale(
            settings_frame,
            from_=60,
            to=200,
            variable=self.width_var,
            orient=tk.HORIZONTAL
        )
        self.width_scale.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=(0, 15))
        
        self.width_label = ttk.Label(settings_frame, text="120", font=('Segoe UI', 11, 'bold'), foreground=self.colors['accent_blue'])
        self.width_label.grid(row=0, column=2, padx=(15, 0), pady=(0, 15))
        
        # FPS ayarı
        fps_label = ttk.Label(settings_frame, text="🎯 Oynatma FPS:", font=('Segoe UI', 11, 'bold'))
        fps_label.grid(row=1, column=0, sticky=tk.W, pady=(0, 15))
        
        self.fps_var = tk.IntVar(value=30)
        self.fps_scale = ttk.Scale(
            settings_frame,
            from_=5,
            to=60,
            variable=self.fps_var,
            orient=tk.HORIZONTAL
        )
        self.fps_scale.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=(0, 15))
        
        self.fps_label = ttk.Label(settings_frame, text="30", font=('Segoe UI', 11, 'bold'), foreground=self.colors['accent_blue'])
        self.fps_label.grid(row=1, column=2, padx=(15, 0), pady=(0, 15))
        
        # Scale değişiklik olayları
        self.width_scale.configure(command=self.update_width_label)
        self.fps_scale.configure(command=self.update_fps_label)
        
        # Tooltip'ler ekle
        self._create_tooltip(self.width_scale, "ASCII çıktının genişliğini ayarlar (60-200 karakter)")
        self._create_tooltip(self.fps_scale, "Video oynatma hızını ayarlar (5-60 FPS)")
        
    def setup_buttons(self):
        """Modern butonlar bölümü"""
        button_frame = ttk.Frame(self.main_frame)
        button_frame.grid(row=3, column=0, columnspan=3, pady=(0, 20))
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        
        # Modern butonlar
        self.info_button = ttk.Button(
            button_frame,
            text="📊 Video Bilgileri",
            style='Modern.TButton',
            command=self.show_video_info
        )
        self.info_button.grid(row=0, column=0, padx=(0, 10), sticky=(tk.W, tk.E))
        
        self.play_button = ttk.Button(
            button_frame,
            text="▶️ ASCII Oynat",
            style='Modern.TButton',
            command=self.play_ascii_video
        )
        self.play_button.grid(row=0, column=1, padx=(0, 10), sticky=(tk.W, tk.E))
        
        self.terminal_button = ttk.Button(
            button_frame,
            text="🖥️ Terminal Aç",
            style='Modern.TButton',
            command=self.open_terminal
        )
        self.terminal_button.grid(row=0, column=2, sticky=(tk.W, tk.E))
        
        # Buton tooltip'leri
        self._create_tooltip(self.info_button, "Seçilen video hakkında detaylı bilgi gösterir")
        self._create_tooltip(self.play_button, "Video'yu ASCII formatında terminal'de oynatır")
        self._create_tooltip(self.terminal_button, "Yeni bir terminal penceresi açar")
        
    def setup_output_area(self):
        """Modern çıktı alanı"""
        output_frame = ttk.LabelFrame(self.main_frame, text="📋 Sistem Çıktısı", style='Modern.TLabelframe', padding="20")
        output_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)
        self.main_frame.rowconfigure(4, weight=1)
        
        # Modern text widget
        self.output_text = tk.Text(
            output_frame,
            height=8,
            bg=self.colors['bg_tertiary'],
            fg=self.colors['accent_green'],
            font=('Consolas', 10),
            wrap=tk.WORD,
            relief='flat',
            borderwidth=0,
            insertbackground=self.colors['accent_blue'],
            selectbackground=self.colors['accent_purple']
        )
        self.output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 5))
        
        # Modern scrollbar
        scrollbar = ttk.Scrollbar(output_frame, orient=tk.VERTICAL, command=self.output_text.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.output_text.configure(yscrollcommand=scrollbar.set)
        
        # Hoş geldin mesajı
        self.log_output("🎥 ASCII Video Player - Modern Edition")
        self.log_output("✨ Hoş geldiniz! Video seçip oynatmaya başlayabilirsiniz.")
        self.log_output("💡 İpucu: Yüksek çözünürlük için genişlik değerini artırın.")
    
    def animate_startup(self):
        """Başlangıç animasyonu"""
        # Başlık animasyonu
        self.root.after(100, self._animate_title)
        
    def _animate_title(self):
        """Başlık animasyonu"""
        try:
            # Başlık rengini değiştir
            title_widgets = self.main_frame.winfo_children()
            for widget in title_widgets:
                if isinstance(widget, ttk.Frame):
                    for child in widget.winfo_children():
                        if isinstance(child, ttk.Label) and "ASCII Video Player" in child.cget("text"):
                            # Renk değişimi animasyonu
                            self.root.after(50, lambda: self._color_cycle(child))
                            break
        except:
            pass
    
    def _color_cycle(self, widget):
        """Renk döngüsü animasyonu"""
        colors = [self.colors['accent_blue'], self.colors['accent_purple'], self.colors['accent_green']]
        for i, color in enumerate(colors):
            self.root.after(i * 200, lambda c=color: self._set_widget_color(widget, c))
    
    def _set_widget_color(self, widget, color):
        """Widget rengini ayarla"""
        try:
            widget.configure(foreground=color)
        except:
            pass
    
    def _create_tooltip(self, widget, text):
        """Modern tooltip oluştur"""
        def show_tooltip(event):
            tooltip = tk.Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
            
            label = tk.Label(tooltip, text=text,
                           background=self.colors['bg_tertiary'],
                           foreground=self.colors['text_primary'],
                           font=('Segoe UI', 9),
                           relief='flat',
                           borderwidth=0,
                           padx=8, pady=4)
            label.pack()
            
            widget.tooltip = tooltip
        
        def hide_tooltip(event):
            if hasattr(widget, 'tooltip'):
                widget.tooltip.destroy()
                del widget.tooltip
        
        widget.bind('<Enter>', show_tooltip)
        widget.bind('<Leave>', hide_tooltip)
        
    def update_width_label(self, value):
        """Genişlik etiketini güncelle"""
        self.width_label.config(text=str(int(float(value))))
        
    def update_fps_label(self, value):
        """FPS etiketini güncelle"""
        self.fps_label.config(text=str(int(float(value))))
        
    def browse_video(self):
        """Video dosyası seç"""
        filetypes = [
            ('Video dosyaları', '*.mp4 *.avi *.mov *.mkv *.wmv *.flv'),
            ('MP4 dosyaları', '*.mp4'),
            ('AVI dosyaları', '*.avi'),
            ('Tüm dosyalar', '*.*')
        ]
        
        filename = filedialog.askopenfilename(
            title="Video dosyası seçin",
            filetypes=filetypes
        )
        
        if filename:
            self.video_path_var.set(filename)
            self.log_output(f"✅ Video seçildi: {os.path.basename(filename)}")
            # Video bilgilerini otomatik göster
            self.root.after(500, self._auto_show_video_info)
    
    def _auto_show_video_info(self):
        """Video seçildikten sonra otomatik bilgi göster"""
        try:
            video_path = self.video_path_var.get()
            if video_path and os.path.exists(video_path):
                player = ASCIIVideoPlayer()
                video_info = player.get_video_info(video_path)
                if video_info:
                    self.log_output(f"📊 Video bilgileri yüklendi: {video_info['width']}x{video_info['height']}, {video_info['fps']:.1f} FPS")
        except Exception as e:
            self.log_output(f"⚠️ Video bilgileri alınamadı: {str(e)}")
            
    def log_output(self, message):
        """Modern çıktı alanına mesaj ekle"""
        # Mesaj tipine göre renk belirle
        if "✅" in message or "success" in message.lower():
            color = self.colors['success']
        elif "❌" in message or "error" in message.lower() or "hata" in message.lower():
            color = self.colors['error']
        elif "⚠️" in message or "warning" in message.lower() or "uyarı" in message.lower():
            color = self.colors['warning']
        elif "🎬" in message or "🎥" in message:
            color = self.colors['accent_blue']
        else:
            color = self.colors['accent_green']
        
        # Mesajı ekle
        self.output_text.insert(tk.END, f"{message}\n")
        
        # Son eklenen satırı renklendir
        start_line = self.output_text.index("end-2l")
        end_line = self.output_text.index("end-1l")
        self.output_text.tag_add("colored", start_line, end_line)
        self.output_text.tag_configure("colored", foreground=color)
        
        # Scroll'u en alta al
        self.output_text.see(tk.END)
        self.root.update_idletasks()
        
    def show_video_info(self):
        """Video bilgilerini göster"""
        video_path = self.video_path_var.get()
        if not video_path:
            messagebox.showwarning("Uyarı", "Lütfen önce bir video dosyası seçin!")
            return
            
        if not os.path.exists(video_path):
            messagebox.showerror("Hata", "Seçilen video dosyası bulunamadı!")
            return
            
        try:
            player = ASCIIVideoPlayer()
            video_info = player.get_video_info(video_path)
            
            if video_info:
                info_text = f"""
📹 Video Bilgileri
📁 Dosya: {os.path.basename(video_path)}
📐 Çözünürlük: {video_info['width']}x{video_info['height']}
🎯 FPS: {video_info['fps']:.2f}
⏱️  Süre: {video_info['duration']:.1f} saniye
🎬 Toplam frame: {video_info['total_frames']}
💾 Codec: {video_info['codec']}
📏 ASCII genişlik: {self.width_var.get()}
🎮 Oynatma FPS: {self.fps_var.get()}
"""
                self.log_output(info_text)
            else:
                self.log_output("❌ Video bilgileri alınamadı!")
                
        except Exception as e:
            self.log_output(f"❌ Hata: {str(e)}")
            
    def play_ascii_video(self):
        """ASCII video oynat"""
        video_path = self.video_path_var.get()
        if not video_path:
            messagebox.showwarning("Uyarı", "Lütfen önce bir video dosyası seçin!")
            return
            
        if not os.path.exists(video_path):
            messagebox.showerror("Hata", "Seçilen video dosyası bulunamadı!")
            return
            
        # Yeni thread'de oynat
        thread = threading.Thread(target=self._play_video_thread)
        thread.daemon = True
        thread.start()
        
    def _play_video_thread(self):
        """Video oynatma thread'i"""
        try:
            video_path = self.video_path_var.get()
            width = self.width_var.get()
            fps = self.fps_var.get()
            
            self.log_output(f"🎬 Video oynatılıyor...")
            self.log_output(f"📏 Genişlik: {width}, 🎯 FPS: {fps}")
            self.log_output("🖥️ Yeni terminal penceresi açılıyor...")
            
            # Windows'ta yeni terminal penceresi aç
            if os.name == 'nt':  # Windows
                cmd = f'start cmd /k "python ascii_video_player.py \"{video_path}\" -w {width} -f {fps}"'
                os.system(cmd)
            else:  # Linux/Mac
                cmd = f'gnome-terminal -- bash -c "python ascii_video_player.py \'{video_path}\' -w {width} -f {fps}; exec bash"'
                os.system(cmd)
            
            self.log_output("✅ Terminal penceresi açıldı!")
            self.log_output("💡 Video yeni pencerede oynatılacak...")
            
        except Exception as e:
            self.log_output(f"❌ Terminal açılamadı: {str(e)}")
            self.log_output("🔄 Alternatif yöntem deneniyor...")
            
            # Alternatif: Mevcut terminal'de çalıştır
            try:
                cmd = [
                    'python', 'ascii_video_player.py',
                    video_path,
                    '-w', str(width),
                    '-f', str(fps)
                ]
                subprocess.run(cmd, check=True)
                self.log_output("✅ Video oynatma tamamlandı!")
            except Exception as e2:
                self.log_output(f"❌ Hata: {str(e2)}")
            
    def open_terminal(self):
        """Terminal penceresi aç"""
        try:
            if os.name == 'nt':  # Windows
                os.system('start cmd /k "cd /d ' + os.getcwd() + '"')
            else:  # Linux/Mac
                os.system('gnome-terminal --working-directory=' + os.getcwd() + ' &')
            self.log_output("🖥️ Yeni terminal penceresi açıldı!")
            self.log_output("📁 Çalışma dizini: " + os.getcwd())
        except Exception as e:
            self.log_output(f"❌ Terminal açılamadı: {str(e)}")
            self.log_output("💡 Manuel olarak terminal açıp şu komutu çalıştırın:")
            self.log_output(f"   python ascii_video_player.py video_dosyasi.mp4")

def main():
    root = tk.Tk()
    app = VideoPlayerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
