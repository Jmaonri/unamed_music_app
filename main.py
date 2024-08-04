import os
import subprocess

link = input("Enter playlist url to download playlist\n")
subprocess.Popen(["yt-dlp", "--yes-playlist", "-x", "--audio-format", "mp3", "-o", f"{os.path.join(os.path.dirname(__file__), 'downloads', '%(title)s.%(ext)s')}", f"{link}"])