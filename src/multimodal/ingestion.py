class MultimodalIngestor:

    def __init__(
        self,
        registry,
        ocr,
        asr,
    ):
        self.registry = registry
        self.ocr = ocr
        self.asr = asr

    def enrich(self, row):

        text = str(
    row.get(
        "message_text",
        "",
    )
)

        if text == "nan":
            text = ""

        media_type = str(
            row.get(
                "media_type",
                "",
            )
        ).lower()

        media_id = row.get(
            "media_id",
            None,
        )

        if media_type == "image":

            path = self.registry.get_image(
                media_id
            )

            ocr_text = self.ocr.extract(path)

            text = f"{text} {ocr_text}"

        elif media_type in [
            "voice",
            "audio",
        ]:

            path = self.registry.get_audio(
                media_id
            )

            transcript = self.asr.transcribe(
                path
            )

            text = f"{text} {transcript}"
            
        print("TYPE:", media_type)
        print("ID:", media_id)
        print("TEXT:", text)

        return text.strip()