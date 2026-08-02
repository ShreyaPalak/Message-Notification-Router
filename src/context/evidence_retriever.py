from difflib import SequenceMatcher


class EvidenceRetriever:

    def __init__(
        self,
        history,
        threshold=0.55,
        top_k=5,
    ):
        self.history = history
        self.threshold = threshold
        self.top_k = top_k

    def similarity(
        self,
        first,
        second,
    ):
        return SequenceMatcher(
            None,
            str(first).lower(),
            str(second).lower(),
        ).ratio()

    def retrieve(
        self,
        user_id,
        text,
    ):

        history = self.history[
            self.history["user_id"] == user_id
        ]

        candidates = []

        for _, row in history.iterrows():

            score = self.similarity(
                text,
                row["message_text"],
            )

            candidates.append(
                (
                    row["message_id"],
                    score,
                )
            )

        candidates.sort(
            key=lambda x: x[1],
            reverse=True,
        )

        return [
            message_id
            for message_id, score in candidates
            if score > self.threshold
        ][: self.top_k]