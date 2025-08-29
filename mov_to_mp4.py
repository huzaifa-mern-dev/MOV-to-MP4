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

def bulk_convert_mov_to_mp4(directory, reencode=False):
    """
    Convert all .mov files in a directory to .mp4
    
    Parameters:
        directory (str): Path to the directory containing .mov files
        reencode (bool): If True, re-encodes. If False, just repackages.
    """
    if not os.path.isdir(directory):
        print(f"❌ Directory not found: {directory}")
        return
    
    mov_files = [f for f in os.listdir(directory) if f.lower().endswith('.mov')]
    
    if not mov_files:
        print(f"❌ No .mov files found in {directory}")
        return
    
    print(f"🔍 Found {len(mov_files)} .mov files")
    
    for mov_file in mov_files:
        input_path = os.path.join(directory, mov_file)
        convert_mov_to_mp4(input_path, reencode=reencode)
    
    print(f"🎉 Bulk conversion complete! Converted {len(mov_files)} files")

def interactive_mode():
    """
    Interactive mode to get user preferences
    """
    print("🎬 MOV to MP4 Converter")
    print("=" * 30)
    
    # Ask for conversion type
    print("\nChoose conversion type:")
    print("1. Single file conversion")
    print("2. Bulk folder conversion")
    
    while True:
        choice = input("\nEnter your choice (1 or 2): ").strip()
        if choice in ['1', '2']:
            break
        print("❌ Please enter 1 or 2")
    
    # Ask for re-encoding preference
    while True:
        reencode_choice = input("\nDo you want to re-encode? (y/n) [default: n]: ").strip().lower()
        if reencode_choice in ['', 'n', 'no', 'y', 'yes']:
            break
        print("❌ Please enter y or n")
    
    reencode = reencode_choice in ['y', 'yes']
    
    if choice == '1':
        # Single file mode
        while True:
            input_file = input("\nEnter path to .mov file: ").strip()
            if os.path.isfile(input_file) and input_file.lower().endswith('.mov'):
                break
            print("❌ File not found or not a .mov file")
        
        output_file = input("Enter output path (press Enter for auto): ").strip()
        if not output_file:
            output_file = None
        
        convert_mov_to_mp4(input_file, output_file, reencode)
    
    else:
        # Bulk mode
        while True:
            directory = input("\nEnter folder path: ").strip()
            if os.path.isdir(directory):
                break
            print("❌ Directory not found")
        
        bulk_convert_mov_to_mp4(directory, reencode)

if __name__ == "__main__":
    # If no arguments provided, run interactive mode
    if len(sys.argv) == 1:
        interactive_mode()
    elif len(sys.argv) >= 2:
        # Check for bulk conversion
        if sys.argv[1] == "--bulk":
            if len(sys.argv) < 3:
                print("❌ Please provide directory path for bulk conversion")
                sys.exit(1)
            
            directory = sys.argv[2]
            reencode = len(sys.argv) > 3 and sys.argv[3] == "--reencode"
            bulk_convert_mov_to_mp4(directory, reencode)
        else:
            # Single file conversion
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
    else:
        print("Usage:")
        print("  Interactive: python mov_to_mp4.py")
        print("  Single file: python mov_to_mp4.py input.mov [output.mp4] [--reencode]")
        print("  Bulk folder: python mov_to_mp4.py --bulk /path/to/folder [--reencode]")
        print("\nExamples:")
        print("  python mov_to_mp4.py")
        print("  python mov_to_mp4.py --bulk /home/user/videos")
        print("  python mov_to_mp4.py --bulk . --reencode")
        sys.exit(1)
