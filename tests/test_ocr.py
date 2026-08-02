from src.multimodal.media_registry import MediaRegistry
from src.multimodal.ocr import OCRExtractor

registry = MediaRegistry(
    "dataset/images.csv",
    "dataset/voice_notes.csv",
    "dataset",
)

ocr = OCRExtractor()

for image_id in sorted(registry.images.keys()):

    path = registry.get_image(image_id)

    print("=" * 70)
    print("IMAGE:", image_id)
    print("PATH:", path)

    try:
        text = ocr.extract(path)

        if text:
            print("\nOCR OUTPUT:")
            print(text)
        else:
            print("\nOCR OUTPUT: <EMPTY>")

    except Exception as e:
        print("\nERROR:")
        print(e)