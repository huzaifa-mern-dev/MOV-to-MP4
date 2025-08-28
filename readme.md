# 🎥 MOV to MP4 Converter (Python + FFmpeg)

A simple Python tool to convert `.mov` video files into `.mp4` using [FFmpeg](https://ffmpeg.org/).  
It supports **fast repackaging (no quality loss)** or **re-encoding (slower but more compatible)**.

---

## ⚡ Features
- Convert `.mov` to `.mp4` easily
- Option to **repackage without re-encoding** (very fast, no quality loss)
- Option to **re-encode with H.264 + AAC** for maximum compatibility
- Works on **Windows, macOS, and Linux**

---

## 📦 Requirements
- Python 3.7+
- [FFmpeg](https://ffmpeg.org/download.html) installed and added to PATH  

### Install FFmpeg
- **Linux (Debian/Ubuntu):**
  ```bash
  sudo apt install ffmpeg

macOS (Homebrew):

brew install ffmpeg


Windows:

Download from FFmpeg.org

Extract the ZIP

Add the bin/ folder path to System PATH

🚀 Usage
1. Clone or Download
git clone https://github.com/yourusername/mov-to-mp4-converter.git
cd mov-to-mp4-converter

2. Run Script
python mov_to_mp4.py input.mov

3. Options

Default (fast, no quality loss):

python mov_to_mp4.py video.mov


→ Outputs video.mp4

Custom output file:

python mov_to_mp4.py video.mov myvideo.mp4


Re-encode (H.264 + AAC):

python mov_to_mp4.py video.mov --reencode


Custom output + re-encode:

python mov_to_mp4.py video.mov myvideo.mp4 --reencode

🛠 Example
python mov_to_mp4.py sample.mov


Output:

⚡ Converting: sample.mov → sample.mp4
✅ Done! Saved as sample.mp4
