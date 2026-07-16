import os
import time

import torch
import soundfile as sf

from transformers import AutoTokenizer
from parler_tts import ParlerTTSForConditionalGeneration

from tts.config import (
    DEVICE,
    MODEL_ID,
    OUTPUT_DIRECTORY,
    DEFAULT_VOICE_DESCRIPTION,
)


class ParlerEngine:

    def __init__(self):

        print("=" * 60)
        print("Loading AI4Bharat Indic Parler-TTS")
        print("=" * 60)

        os.makedirs(
            OUTPUT_DIRECTORY,
            exist_ok=True,
        )

        print("Loading Tokenizer...")

        self.tokenizer = AutoTokenizer.from_pretrained(
            MODEL_ID
        )

        print("Loading Model...")

        self.model = (
            ParlerTTSForConditionalGeneration
            .from_pretrained(MODEL_ID)
            .to(DEVICE)
        )

        self.model.eval()

        print("Device :", DEVICE)

        print("AI4Bharat Parler-TTS Ready")

        print("=" * 60)

    def synthesize(
        self,
        text,
        filename="output.wav",
        description=DEFAULT_VOICE_DESCRIPTION,
    ):

        print("\nGenerating Speech...")

        start = time.time()

        try:

            description_inputs = self.tokenizer(
                description,
                return_tensors="pt",
                padding=True,
                truncation=True,
            )

            prompt_inputs = self.tokenizer(
                text,
                return_tensors="pt",
                padding=True,
                truncation=True,
            )

            description_inputs = {
                k: v.to(DEVICE)
                for k, v in description_inputs.items()
            }

            prompt_inputs = {
                k: v.to(DEVICE)
                for k, v in prompt_inputs.items()
            }

            with torch.no_grad():

                audio = self.model.generate(

                    input_ids=description_inputs["input_ids"],

                    attention_mask=description_inputs["attention_mask"],

                    prompt_input_ids=prompt_inputs["input_ids"],

                    prompt_attention_mask=prompt_inputs["attention_mask"],

                )

            audio = audio.cpu().numpy().squeeze()

            output_path = os.path.join(
                OUTPUT_DIRECTORY,
                filename,
            )

            sf.write(

                output_path,

                audio,

                self.model.config.sampling_rate,

            )

            total = round(
                time.time() - start,
                2,
            )

            print("Speech Generated Successfully")

            print("Saved :", output_path)

            return {

                "status": "success",

                "audio_path": output_path,

                "processing_time": total,

                "sample_rate": self.model.config.sampling_rate,

            }

        except Exception as e:

            return {

                "status": "error",

                "message": str(e),

            }