import pandas as pd

from src.multimodal.media_registry import MediaRegistry
from src.multimodal.ocr import OCRExtractor
from src.multimodal.asr import WhisperTranscriber
from src.multimodal.ingestion import MultimodalIngestor

registry = MediaRegistry(
    "dataset/images.csv",
    "dataset/voice_notes.csv",
    "dataset",
)

ocr = OCRExtractor()
asr = WhisperTranscriber()

ingestor = MultimodalIngestor(
    registry,
    ocr,
    asr,
)

messages = pd.read_csv("dataset/messages.csv")

print(messages.columns.tolist())
print()

for index, row in messages.head(10).iterrows():

    print("=" * 60)
    print("ROW:", index)

    print("media_type:", row.get("media_type"))
    print("media_id:", row.get("media_id"))

    result = ingestor.enrich(row)

    print("TEXT:")
    print(repr(result))