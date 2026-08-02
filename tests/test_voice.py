from src.multimodal.media_registry import MediaRegistry
from src.multimodal.asr import WhisperTranscriber

registry = MediaRegistry(
    "dataset/images.csv",
    "dataset/voice_notes.csv",
    "dataset",
)

asr = WhisperTranscriber()

for voice_id in sorted(registry.audio.keys()):

    path = registry.get_audio(voice_id)

    print("=" * 70)
    print("VOICE:", voice_id)
    print("PATH:", path)

    try:
        text = asr.transcribe(path)

        if text:
            print("\nTRANSCRIPT:")
            print(text)
        else:
            print("\nTRANSCRIPT: <EMPTY>")

    except Exception as e:
        print("\nERROR:")
        print(e)