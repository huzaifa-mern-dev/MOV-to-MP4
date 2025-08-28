import os
import subprocess
import sys

def convert_mov_to_mp4(input_file, output_file=None, reencode=False):
    """
    Convert .mov video to .mp4 using FFmpeg.
    
    Parameters:
        input_file (str): Path to the input .mov file
        output_file (str): Path to the output .mp4 file (optional)
        reencode (bool): If True, re-encodes (slower but more compatible).
                         If False, just repackages (faster, no quality loss).
    """
    if not os.path.isfile(input_file):
        print(f"❌ File not found: {input_file}")
        return

    if output_file is None:
        base, _ = os.path.splitext(input_file)
        output_file = base + ".mp4"

    if reencode:
        command = [
            "ffmpeg", "-i", input_file,
            "-c:v", "libx264",
            "-c:a", "aac",
            "-strict", "experimental",
            output_file
        ]
    else:
        # Just repackaging (very fast, no quality loss)
        command = ["ffmpeg", "-i", input_file, "-c", "copy", output_file]

    try:
        print(f"⚡ Converting: {input_file} → {output_file}")
        subprocess.run(command, check=True)
        print(f"✅ Done! Saved as {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Conversion failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mov_to_mp4.py input.mov [output.mp4] [--reencode]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = None
    reencode = False

    if len(sys.argv) >= 3:
        if sys.argv[2] == "--reencode":
            reencode = True
        else:
            output_file = sys.argv[2]

    if len(sys.argv) == 4 and sys.argv[3] == "--reencode":
        reencode = True

    convert_mov_to_mp4(input_file, output_file, reencode)
