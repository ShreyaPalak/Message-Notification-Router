import os

from src.config import FFMPEG_BIN

os.environ["PATH"] += os.pathsep + FFMPEG_BIN

class WhisperTranscriber:
    def __init__(self):
        self.available = False

        try:
            import whisper

            self.model = whisper.load_model("base")

            self.available = True

        except Exception:
            self.available = False

    def transcribe(self, path):
        if path is None:
            return ""

        if not self.available:
            return ""

        try:
            result = self.model.transcribe(str(path))
            
            print(result)

            return result["text"].strip()

        except Exception as e:
            print("ERROR:", e)
            return ""