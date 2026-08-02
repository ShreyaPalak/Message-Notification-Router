from src.multimodal.media_registry import MediaRegistry

registry = MediaRegistry(
    "dataset/images.csv",
    "dataset/voice_notes.csv",
    "dataset",
)

print("Images:", len(registry.images))
print("Audio:", len(registry.audio))