from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODELS = {
    "en_indic": "Raghavan/indictrans2-en-indic-dist-200M",
    "indic_en": "Raghavan/indictrans2-indic-en-dist-200M",
}

for folder, repo in MODELS.items():
    print(f"\nDownloading {repo}...")

    tokenizer = AutoTokenizer.from_pretrained(
        repo,
        trust_remote_code=True,
    )

    model = AutoModelForSeq2SeqLM.from_pretrained(
        repo,
        trust_remote_code=True,
    )

    tokenizer.save_pretrained(f"models/translation/{folder}")
    model.save_pretrained(f"models/translation/{folder}")

    print(f"{folder} downloaded successfully.")

print("\nAll translation models downloaded.")