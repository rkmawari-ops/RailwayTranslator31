from stt.speech_to_text import SpeechToText


class SpeechService:

    def __init__(self):
        self.stt = SpeechToText()

    def transcribe(self, audio_path):
        return self.stt.transcribe(audio_path)