from ai.whisper_model import WhisperManager
from ai.translation_model import TranslationManager
from ai.tts_model import TTSManager


class AIManager:

    def __init__(self):

        print("=" * 50)
        print("Initializing AI Manager")
        print("=" * 50)

        self.whisper = WhisperManager()
        self.translation = TranslationManager()
        self.tts = TTSManager()

        print("\nAI Manager Ready")