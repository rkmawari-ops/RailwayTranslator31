from ai.model_registry import ModelRegistry

from ai.whisper_model import WhisperManager
from ai.translation_model import TranslationManager
from ai.tts_model import TTSManager


class AIManager:

    def __init__(self):

        print("=" * 60)
        print("Initializing AI Manager")
        print("=" * 60)

        self.registry = ModelRegistry()

        whisper = WhisperManager()
        translation = TranslationManager()
        tts = TTSManager()

        self.registry.register("whisper", whisper)
        self.registry.register("translation", translation)
        self.registry.register("tts", tts)

        print("\nAI Manager Ready")

    def get_model(self, name):
        return self.registry.get(name)