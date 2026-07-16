import os
import time
from datetime import datetime

from faster_whisper import WhisperModel

from stt.config import (
    MODEL_PATH,
    DEVICE,
    COMPUTE_TYPE,
    BEAM_SIZE,
)

from stt.logger import logger


class SpeechToText:

    def __init__(self):

        print("Loading Whisper model...")

        self.model = WhisperModel(
            MODEL_PATH,
            device=DEVICE,
            compute_type=COMPUTE_TYPE
        )

        print("Whisper loaded successfully.\n")

        logger.info("Whisper model loaded successfully.")

    def transcribe(self, audio_path):

        try:

            if not os.path.exists(audio_path):

                return {
                    "status": "error",
                    "message": "Audio file not found."
                }

            start_time = time.time()

            segments, info = self.model.transcribe(
                audio_path,
                beam_size=BEAM_SIZE
            )

            recognized_text = ""

            for segment in segments:
                recognized_text += segment.text.strip() + " "

            end_time = time.time()

            result = {

                "status": "success",

                "timestamp":
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

                "audio_file": audio_path,

                "language": info.language,

                "confidence":
                round(info.language_probability * 100, 2),

                "recognized_text":
                recognized_text.strip(),

                "processing_time":
                round(end_time - start_time, 2)
            }

            logger.info(
                f"Language={result['language']} | "
                f"Confidence={result['confidence']} | "
                f"Text={result['recognized_text']}"
            )

            return result

        except Exception as e:

            logger.exception("Speech recognition failed.")

            return {
                "status": "error",
                "message": str(e)
            }