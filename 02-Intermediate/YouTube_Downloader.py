import yt_dlp
import os
import sys

# =========================
# Terminal Colors
# =========================
class Color:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

# =========================
# Header
# =========================
print(f"{Color.RED}{Color.BOLD}")
print("==========================")
print("     YouTube Downloader   ")
print("==========================")
print(f"{Color.END}")

# =========================
# Progress Hook
# =========================
def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '').strip()
        speed = d.get('_speed_str', '').strip()
        eta = d.get('_eta_str', '').strip()
        sys.stdout.write(f"\rDownloading: {percent} | Speed: {speed} | ETA: {eta}")
        sys.stdout.flush()
    elif d['status'] == 'finished':
        print("\nDownload completed. Merging files...")

# =========================
# Download function
# =========================
def download_highest_quality(url, save_path, file_type):
    if file_type.lower() == "mp3":
        ydl_opts = {
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'format': 'bestaudio/best',
            'progress_hooks': [progress_hook],
            'quiet': True,
            'no_warnings': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    else:  # mp4
        ydl_opts = {
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'progress_hooks': [progress_hook],
            'quiet': True,
            'no_warnings': True,
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print(f"\n{Color.GREEN}Download finished successfully!{Color.END}")

# =========================
# User Inputs
# =========================
url = input("Enter video or playlist URL: ").strip()

print("\nChoose File Type:")
print("1 - MP4 (Video)")
print("2 - MP3 (Audio only)")
file_choice = input("Your choice: ").strip()
file_type = "mp4" if file_choice != "2" else "mp3"

save_path = "/home/youssef-yaser/Videos/Youtube videos"
os.makedirs(save_path, exist_ok=True)

print(f"\nSaving to: {Color.CYAN}{save_path}{Color.END}")
print(f"File Type: {Color.GREEN}{file_type.upper()}{Color.END}\n")

download_highest_quality(url, save_path, file_type)
