import os
import yt_dlp

def download_audio_from_url(url: str, output_folder: str = "output") -> str:
    """
    Download audio directly from a URL (YouTube, TikTok, Instagram, etc.)
    Returns the path of the saved audio file.
    """
    os.makedirs(output_folder, exist_ok=True)

    # Use a fixed simple filename to avoid special character issues
    audio_path = os.path.join(output_folder, "downloaded_audio.mp3")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_folder, "downloaded_audio.%(ext)s"),
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "quiet": False,
    }

    print(f"Downloading audio from: {url}")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(url, download=True)

    print(f"Audio saved to: {audio_path}")
    return audio_path