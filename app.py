import streamlit as st
import os
from audio_extractor import extract_audio
from transcriber import transcribe_audio
from url_downloader import download_audio_from_url

# --- Page Config ---
st.set_page_config(
    page_title="Video Transcriber",
    page_icon="🎬",
    layout="centered"
)

# --- Title ---
st.title("🎬 Video Transcriber")
st.markdown("Extract audio and transcript from any video — upload a file or paste a URL.")

# --- Input Method ---
option = st.radio("Choose input method:", ["📁 Upload MP4 File", "🔗 Paste Video URL"])

audio_path = None

# --- MP4 Upload ---
if option == "📁 Upload MP4 File":
    uploaded_file = st.file_uploader("Upload your MP4 file", type=["mp4"])

    if uploaded_file is not None:
        # Save uploaded file temporarily
        temp_path = os.path.join("output", "temp_video.mp4")
        os.makedirs("output", exist_ok=True)
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.read())
        st.success("File uploaded successfully!")

        if st.button("Extract & Transcribe"):
            with st.spinner("Extracting audio..."):
                audio_path = extract_audio(temp_path)
            st.success("Audio extracted!")

# --- URL Input ---
elif option == "🔗 Paste Video URL":
    url = st.text_input("Paste YouTube / TikTok / Instagram URL:")

    if url:
        if st.button("Extract & Transcribe"):
            with st.spinner("Downloading audio from URL..."):
                audio_path = download_audio_from_url(url)
            st.success("Audio downloaded!")

# --- Transcribe & Show Results ---
if audio_path and os.path.exists(audio_path):
    with st.spinner("Transcribing... this may take a few minutes ⏳"):
        transcript_path = transcribe_audio(audio_path)

    st.success("Transcription complete! ✅")

    # Show transcript
    with open(transcript_path, "r", encoding="utf-8") as f:
        transcript_text = f.read()

    st.subheader("📝 Transcript")
    st.text_area("", transcript_text, height=300)

  # Audio Player
    st.subheader("🎵 Audio Player")
    with open(audio_path, "rb") as f:
        audio_bytes = f.read()
    st.audio(audio_bytes, format="audio/mp3")

    # Download buttons
    st.subheader("⬇️ Downloads")
    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            label="⬇️ Download Audio (MP3)",
            data=audio_bytes,
            file_name="audio.mp3",
            mime="audio/mpeg"
        )

    with col2:
        st.download_button(
            label="⬇️ Download Transcript (TXT)",
            data=transcript_text,
            file_name="transcript.txt",
            mime="text/plain"
        )