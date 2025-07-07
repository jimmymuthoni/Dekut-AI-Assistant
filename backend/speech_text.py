import whisper
import tempfile
import pyttsx3

model = whisper.load_model("base")

def transcribe(audio_bytes: bytes) -> str:
    """
    Transcribe audio bytes to text using Whisper.
    """
    with tempfile.NamedTemporaryFile(suffix=".wav") as temp_audio:
        temp_audio.write(audio_bytes)
        temp_audio.flush()
        result = model.transcribe(temp_audio.name)
    return result["text"]

def synthesize(text: str) -> bytes:
    """
    Synthesize speech from text using pyttsx3 and return audio bytes.
    """
    engine = pyttsx3.init()
    with tempfile.NamedTemporaryFile(suffix=".mp3") as fp:
        engine.save_to_file(text, fp.name)
        engine.runAndWait()
        fp.seek(0)
        audio_bytes = fp.read()
    return audio_bytes
