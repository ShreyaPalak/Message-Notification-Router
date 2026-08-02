from difflib import SequenceMatcher


class EvidenceRetriever:

    def __init__(self, history):
        self.history = history

    def similarity(self, text1, text2):

        if not text1 or not text2:
            return 0.0

        return SequenceMatcher(
            None,
            str(text1).lower(),
            str(text2).lower(),
        ).ratio()

    def retrieve(self, text, top_k=5):

        if self.history.empty:
            return []

        matches = []

        for _, row in self.history.iterrows():

            candidate = str(
                row.get("message_text", "")
            )

            score = self.similarity(
                text,
                candidate,
            )

            if score > 0.50:

                matches.append(
                    (
                        score,
                        row.get("message_id"),
                    )
                )

        matches.sort(
            key=lambda x: x[0],
            reverse=True,
        )

        return [
            message_id
            for _, message_id in matches[:top_k]
        ]