from translation.models import (
    TranslationRequest,
    TranslationResult,
)


class TranslationEngine:

    def __init__(self):
        print("Translation Engine Initialized")

    def translate(
        self,
        request: TranslationRequest,
    ):

        return TranslationResult(
            status="success",
            source_language=request.source_language,
            target_language=request.target_language,
            original_text=request.text,
            translated_text=request.text,
            processing_time=0.0,
        )