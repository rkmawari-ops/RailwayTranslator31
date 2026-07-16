from translation.offline_provider import (
    OfflineTranslationProvider
)

from translation.models import (
    TranslationRequest
)


class TranslationService:

    def __init__(self):

        self.provider = (
            OfflineTranslationProvider()
        )

        self.provider.load()

    def translate(
        self,
        text,
        source,
        target
    ):

        request = TranslationRequest(

            text=text,

            source_language=source,

            target_language=target
        )

        return self.provider.translate(
            request
        )