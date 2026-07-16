from abc import ABC, abstractmethod

from translation.models import (
    TranslationRequest,
    TranslationResult,
)


class BaseTranslator(ABC):

    @abstractmethod
    def translate(
        self,
        request: TranslationRequest,
    ) -> TranslationResult:
        pass