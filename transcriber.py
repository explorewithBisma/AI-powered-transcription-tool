import os
import whisper

def transcribe_audio(audio_path: str, output_folder: str = "output") -> str:
    """
    Transcribe audio file to text using Whisper.
    Returns the path of the saved transcript file.
    """
    os.makedirs(output_folder, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(audio_path))[0]
    transcript_path = os.path.join(output_folder, base_name + ".txt")

    print("Loading Whisper model...")
    model = whisper.load_model("base")

    print("Transcribing... (may take a minute)")
    result = model.transcribe(audio_path)
    text = result["text"]

    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Transcript saved to: {transcript_path}")
    return transcript_path