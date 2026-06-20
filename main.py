import argparse
import os
from audio_extractor import extract_audio
from transcriber import transcribe_audio
from url_downloader import download_audio_from_url

def is_url(text: str) -> bool:
    """Check if input is a URL or a file path."""
    return text.startswith("http://") or text.startswith("https://")

def main():
    parser = argparse.ArgumentParser(description="Extract audio and transcribe video")
    parser.add_argument("input", help="MP4 file path OR video URL (YouTube, TikTok, Instagram)")
    parser.add_argument("--no-transcribe", action="store_true", help="Skip transcription")
    args = parser.parse_args()

    # Step 1: Get audio (from file or URL)
    if is_url(args.input):
        print("URL detected — downloading audio...")
        audio_path = download_audio_from_url(args.input)
    else:
        if not os.path.isfile(args.input):
            raise FileNotFoundError(f"File not found: {args.input}")
        print("File detected — extracting audio...")
        audio_path = extract_audio(args.input)

    # Step 2: Transcribe
    if not args.no_transcribe:
        transcribe_audio(audio_path)

    print("\nDone! Check the output/ folder for your files.")

if __name__ == "__main__":
    main()