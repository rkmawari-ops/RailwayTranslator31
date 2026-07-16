from translation.engine import TranslationEngine
from translation.models import TranslationRequest


class TranslationService:

    def __init__(self):
        self.engine = TranslationEngine()

    def translate(self, text, source, target):

        request = TranslationRequest(
            text=text,
            source_language=source,
            target_language=target,
        )

        return self.engine.translate(request)