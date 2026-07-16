from stt.speech_to_text import SpeechToText


class WhisperManager:

    def __init__(self):
        print("Loading Whisper Model...")

        self.stt = SpeechToText()

        print("Whisper Model Ready")

    def transcribe(self, audio_path):
        return self.stt.transcribe(audio_path)