import time
import argostranslate.translate

from translation.provider import TranslationProvider
from translation.models import (
    TranslationRequest,
    TranslationResult,
)


class OfflineTranslationProvider(TranslationProvider):

    def load(self):
        print("Loading Argos Translation Provider...")
        print("Argos Translation Ready")

    def translate(
        self,
        request: TranslationRequest
    ) -> TranslationResult:

        start = time.time()

        translated = argostranslate.translate.translate(
            request.text,
            request.source_language,
            request.target_language
        )

        return TranslationResult(
            status="success",
            source_language=request.source_language,
            target_language=request.target_language,
            original_text=request.text,
            translated_text=translated,
            processing_time=round(time.time() - start, 3),
        )