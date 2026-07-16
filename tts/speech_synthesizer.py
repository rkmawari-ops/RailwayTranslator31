import os
import time

import torch
from TTS.api import TTS

from tts.config import (
    MODEL_NAME,
    DEVICE,
    OUTPUT_DIRECTORY,
)


class SpeechSynthesizer:

    def __init__(self):

        print("=" * 60)
        print("Loading XTTS Model...")
        print("=" * 60)

        self.device = DEVICE if torch.cuda.is_available() else "cpu"

        self.tts = TTS(MODEL_NAME).to(self.device)

        os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

        print(f"XTTS Loaded on {self.device}")

    def synthesize(
        self,
        text,
        language="hi",
        speaker_wav=None,
        output_filename="output.wav",
    ):

        start = time.time()

        output_path = os.path.join(
            OUTPUT_DIRECTORY,
            output_filename,
        )

        kwargs = {
            "text": text,
            "language": language,
            "file_path": output_path,
        }

        # XTTS voice cloning (optional)
        if speaker_wav:
            kwargs["speaker_wav"] = speaker_wav

        self.tts.tts_to_file(**kwargs)

        return {
            "status": "success",
            "audio_path": output_path,
            "processing_time": round(time.time() - start, 2),
        }