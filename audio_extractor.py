
import os
from moviepy import VideoFileClip

def extract_audio(video_path: str, output_folder: str = "output") -> str:
    """
    Extract audio from an MP4 file.
    Returns the path of the saved audio file.
    """
    os.makedirs(output_folder, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(video_path))[0]
    audio_path = os.path.join(output_folder, base_name + ".mp3")

    print(f"Extracting audio from: {video_path}")

    with VideoFileClip(video_path) as clip:
        if clip.audio is None:
            raise ValueError("No audio track found in this video.")
        clip.audio.write_audiofile(audio_path)

    print(f"Audio saved to: {audio_path}")
    return audio_path