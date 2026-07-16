from translation.translation_service import TranslationService


class TranslationManager:

    def __init__(self):

        print("=" * 60)
        print("Loading Argos Translation")
        print("=" * 60)

        self.engine = TranslationService()

        print("Argos Translation Ready")

    def translate(
        self,
        text,
        source,
        target,
    ):

        return self.engine.translate(
            text,
            source,
            target,
        )