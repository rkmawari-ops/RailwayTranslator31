from tts.parler_engine import ParlerEngine


class TTSManager:

    def __init__(self):

        print("=" * 60)
        print("Loading AI4Bharat TTS")
        print("=" * 60)

        self.engine = ParlerEngine()

        print("AI4Bharat Ready")

    def synthesize(
        self,
        text,
        filename="output.wav",
    ):

        return self.engine.synthesize(

            text=text,

            filename=filename,

        )