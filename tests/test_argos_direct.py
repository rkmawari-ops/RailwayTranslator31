import argostranslate.translate

tests = [
    "Hello",
    "Hello? Hello? Hello?",
    "Where is Platform Number Five?",
]

for text in tests:
    print("=" * 50)
    print("Original :", text)

    translated = argostranslate.translate.translate(
        text,
        "en",
        "hi",
    )

    print("Translated :", translated)