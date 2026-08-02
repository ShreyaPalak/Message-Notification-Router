from src.multimodal.media_registry import MediaRegistry
from src.multimodal.asr import WhisperTranscriber

registry = MediaRegistry(
    "dataset/images.csv",
    "dataset/voice_notes.csv",
    "dataset",
)

asr = WhisperTranscriber()

voice_id = "vn_001"

path = registry.get_audio(voice_id)

print(path)

print(asr.transcribe(path))