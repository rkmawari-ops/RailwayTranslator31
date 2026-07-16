from ai.manager import AIManager
from services.audio_player import AudioPlayer
from core.session import ConversationSession
from core.language_manager import get_language_name


class PipelineController:

    def __init__(self):

        print("=" * 60)
        print("Initializing Railway Translation Pipeline")
        print("=" * 60)

        self.ai = AIManager()

        self.whisper = self.ai.get_model("whisper")
        self.translation = self.ai.get_model("translation")
        self.tts = self.ai.get_model("tts")

        self.player = AudioPlayer()

        self.session = ConversationSession()

        # --------------------------------------------------
        # TEMPORARY
        # Until the GUI is built, the operator language
        # is fixed to Hindi.
        # --------------------------------------------------
        self.session.operator_language = "hi"

    def process_audio(
        self,
        audio_path,
    ):

        # ==================================================
        # STEP 1 : Speech Recognition
        # ==================================================

        print("\n" + "=" * 60)
        print("STEP 1 : Speech Recognition")
        print("=" * 60)

        speech = self.whisper.transcribe(audio_path)

        if speech["status"] != "success":
            return speech

        self.session.start(speech["language"])

        print("\nDetected Passenger Language")
        print("-" * 40)
        print(get_language_name(speech["language"]))

        print("\nRecognized Text")
        print("-" * 40)
        print(speech["recognized_text"])

        # ==================================================
        # STEP 2 : Translation
        # ==================================================

        print("\n" + "=" * 60)
        print("STEP 2 : Translation")
        print("=" * 60)

        print("\nTranslation Route")
        print("-" * 40)
        print(
            f'{speech["language"]} --> {self.session.operator_language}'
        )

        translated = self.translation.translate(
            text=speech["recognized_text"],
            source=speech["language"],
            target=self.session.operator_language,
        )

        print("\nTranslation Object")
        print("-" * 40)
        print(translated)

        if translated.status != "success":
            return translated

        print("\nTranslated Text")
        print("-" * 40)
        print(translated.translated_text)

        # ==================================================
        # STEP 3 : Text To Speech
        # ==================================================

        print("\n" + "=" * 60)
        print("STEP 3 : Speech Synthesis")
        print("=" * 60)

        tts = self.tts.synthesize(
            text=translated.translated_text,
            filename="translated.wav",
        )

        if tts["status"] != "success":
            return tts

        print("\nGenerated Audio")
        print("-" * 40)
        print(tts["audio_path"])

        # ==================================================
        # STEP 4 : Play Audio
        # ==================================================

        print("\n" + "=" * 60)
        print("STEP 4 : Playing Audio")
        print("=" * 60)

        self.player.play(tts["audio_path"])

        self.session.update()

        print("\n" + "=" * 60)
        print("PIPELINE COMPLETED SUCCESSFULLY")
        print("=" * 60)

        return {
            "speech": speech,
            "translation": translated,
            "tts": tts,
            "session": self.session,
        }