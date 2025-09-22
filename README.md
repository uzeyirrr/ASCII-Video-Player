# 🎥 ASCII Video Player - Modern Edition

<div align="center">

![ASCII Video Player](https://img.shields.io/badge/ASCII-Video%20Player-blue?style=for-the-badge&logo=terminal)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-red?style=for-the-badge&logo=opencv)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**The most modern way to play videos in terminal! 🚀**

[![GitHub stars](https://img.shields.io/github/stars/uzeyirrr/ASCII-Video-Player?style=social)](https://github.com/uzeyirrr/ASCII-Video-Player)
[![GitHub forks](https://img.shields.io/github/forks/uzeyirrr/ASCII-Video-Player?style=social)](https://github.com/uzeyirrr/ASCII-Video-Player)

</div>

This project allows you to **play videos in ASCII format in the console**.  
Each frame is converted to grayscale and mapped to specific ASCII characters, creating a fluid video effect displayed in the terminal with modern features and high resolution.

## 🎬 Demo

```
🎥 ASCII Video Player
Frame: 15/30
--------------------------------------------------
    ░▒▓█▄▀▌▐▔▕▖▗▘▙▚▛▜▝▞▟■□▢▣▤▥▦▧▨▩▪▫▬▭▮▯▰▱
    ▲△▴▵▶▷▸▹►▻▼▽▾▿◀◁◂◃◄◅◆◇◈◉◊○◌◍◎●◐◑◒◓◔◕
    ◖◗◘◙◚◛◜◝◞◟◠◡◢◣◤◥◦◧◨◩◪◫◬◭◮◯◰◱◲◳◴◵◶◷
    ◸◹◺◻◼◽◾◿ .'`^",:;Il!i><~+_-?][}{1)(|\/
    tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$
```

## ✨ Features

### 🖥️ Modern Interface
- **Ultra Modern GUI** - Dark theme, animations, and tooltips
- **Responsive Design** - Adapts to different screen sizes
- **Smart Tooltip System** - Help for every feature
- **Colored Output** - Message type-based coloring

### 🎬 Video Processing
- **High Resolution ASCII** - 70 characters for detailed display
- **CLAHE Contrast Enhancement** - Image quality optimization
- **Gaussian Blur** - Smoothing while preserving details
- **Smart Video Analysis** - Automatic metadata and info display

### ⚙️ Advanced Settings
- **Dynamic Width** - Adjustable 60-200 characters
- **FPS Control** - 5-60 FPS playback speed
- **Vertical Video Support** - Automatic centering and visibility
- **Flicker Prevention** - Smooth playback and cursor optimization

### 💻 Platform Support
- **Multi-Platform** - Windows, Linux, Mac support
- **Auto-Launch** - Batch and bash scripts
- **Error Management** - Comprehensive error control and reporting

## 🚀 Quick Start

### 📋 Requirements
- Python 3.8+
- OpenCV 4.8+
- Tkinter (comes with Python)
- Colorama

### ⚡ First Time Setup
**You need to install the required packages first:**

```bash
# Install all required dependencies
pip install -r requirements.txt

# Or install manually
pip install opencv-python colorama
```

### 🖥️ Modern GUI (Recommended)

#### Windows
```bash
# Auto-launch (recommended)
start_gui.bat

# Manual launch
python video_player_gui.py
```

#### Linux/Mac
```bash
# Auto-launch (recommended)
./start_gui.sh

# Manual launch
python3 video_player_gui.py
```

**🎨 Modern GUI Features:**
- 🌙 Dark theme and modern color palette
- ✨ Animated title and hover effects
- 💡 Smart tooltips and help system
- 📊 Automatic video info analysis
- 🎨 Colored system output
- 📱 Responsive design

### 💻 Command Line

#### Basic Usage
```bash
python ascii_video_player.py video.mp4
```

#### Advanced Options
```bash
# High resolution
python ascii_video_player.py video.mp4 -w 150

# Custom FPS
python ascii_video_player.py video.mp4 -f 24

# Show video info
python ascii_video_player.py video.mp4 --info

# Combination
python ascii_video_player.py video.mp4 -w 120 -f 30
```

## 📖 Installation

### Method 1: Clone Repository (Recommended)
```bash
# Clone the repository
git clone https://github.com/uzeyirrr/ASCII-Video-Player.git
cd ASCII-Video-Player

# Install required dependencies
pip install -r requirements.txt
```

### Method 2: Direct Download
```bash
# Download the files manually
# Then install dependencies
pip install opencv-python colorama
```

### ⚠️ Important Notes
- **Always install requirements first** before running the application
- Make sure you have Python 3.8+ installed
- On some systems, you might need to use `pip3` instead of `pip`

## 🎮 Usage Examples

### GUI Mode
1. **First, install requirements:** `pip install -r requirements.txt`
2. Run `start_gui.bat` (Windows) or `./start_gui.sh` (Linux/Mac)
3. Select your video file
4. Adjust width and FPS settings
5. Click "ASCII Play" to start

### Command Line Mode
```bash
# Basic video playback
python ascii_video_player.py my_video.mp4

# High quality playback
python ascii_video_player.py my_video.mp4 -w 200 -f 30

# Show video information only
python ascii_video_player.py my_video.mp4 --info
```

## 🔧 Configuration

### ASCII Character Set
The player uses 70 different ASCII characters for high-resolution display:
```
 .'`^",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$
```

### Supported Video Formats
- MP4, AVI, MOV, MKV, WMV, FLV
- All formats supported by OpenCV

## 🐛 Troubleshooting

### Common Issues

**GUI won't start:**
```bash
# Check Python installation
python --version

# Install missing dependencies (MOST COMMON ISSUE)
pip install -r requirements.txt

# If still not working, try:
pip install opencv-python colorama
```

**Video not playing:**
- Check video file path
- Ensure video format is supported
- Try with `--info` flag to check video properties

**Poor quality output:**
- Increase width parameter (`-w 150`)
- Check terminal size and font
- Ensure good contrast in terminal

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenCV for video processing
- Tkinter for GUI framework
- Colorama for terminal colors
- All contributors and users

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ for the terminal community

</div>  