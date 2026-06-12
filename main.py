import argparse
from audio_extractor import extract_audio
from transcriber import transcribe_audio

def main():
    parser = argparse.ArgumentParser(description="Extract audio and transcribe video")
    parser.add_argument("input", help="Path to your MP4 video file")
    parser.add_argument("--no-transcribe", action="store_true", help="Skip transcription")
    args = parser.parse_args()

    audio_path = extract_audio(args.input)

    if not args.no_transcribe:
        transcribe_audio(audio_path)

    print("\nDone! Check the output/ folder for your files.")

if __name__ == "__main__":
    main()