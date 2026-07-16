import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

MODEL_ID = "ai4bharat/indic-parler-tts"

OUTPUT_DIRECTORY = "assets/output_audio"

DEFAULT_VOICE_DESCRIPTION = (
    "A female Indian railway announcer speaking in a clear, natural, calm voice "
    "with accurate pronunciation suitable for public announcements."
)