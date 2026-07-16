from translation.engine import TranslationEngine
from translation.models import TranslationRequest


engine = TranslationEngine()

request = TranslationRequest(
    text="Where is Platform Number Five?",
    source_language="en",
    target_language="hi",
)

result = engine.translate(request)

print("\n========================")
print("Translation Result")
print("========================")

print(result.model_dump())