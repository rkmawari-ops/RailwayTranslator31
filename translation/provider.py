from abc import ABC, abstractmethod

from translation.models import (
    TranslationRequest,
    TranslationResult
)


class TranslationProvider(ABC):

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def translate(
        self,
        request: TranslationRequest
    ) -> TranslationResult:
        pass