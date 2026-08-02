from pathlib import Path

import pandas as pd


class MediaRegistry:

    def __init__(
        self,
        images_csv,
        voice_csv,
        dataset_root,
    ):
        self.dataset_root = Path(dataset_root)

        self.images = {}
        self.audio = {}

        self._load_images(images_csv)
        self._load_audio(voice_csv)

    def _load_images(self, path):

        df = pd.read_csv(path)

        for _, row in df.iterrows():

            image_id = row["image_id"]

            file_path = (
                self.dataset_root / row["file_path"]
            )

            self.images[image_id] = file_path

    def _load_audio(self, path):

        df = pd.read_csv(path)

        for _, row in df.iterrows():

            voice_id = row["voice_note_id"]

            file_path = (
                self.dataset_root / row["file_path"]
            )

            self.audio[voice_id] = file_path

    def get_image(self, image_id):

        return self.images.get(image_id)

    def get_audio(self, audio_id):

        return self.audio.get(audio_id)