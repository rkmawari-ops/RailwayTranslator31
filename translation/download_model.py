from pathlib import Path

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

MODEL_NAME = "ai4bharat/indictrans2-en-indic-1B"

MODEL_DIR = Path("models/translation/indictrans2")

MODEL_DIR.mkdir(parents=True, exist_ok=True)

print("Downloading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

print("Downloading model...")
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

print("Saving locally...")

tokenizer.save_pretrained(MODEL_DIR)
model.save_pretrained(MODEL_DIR)

print("\nModel downloaded successfully!")
print(f"Saved to: {MODEL_DIR}")