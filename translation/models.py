from pydantic import BaseModel


class TranslationRequest(BaseModel):
    text: str
    source_language: str
    target_language: str


class TranslationResult(BaseModel):
    status: str
    source_language: str
    target_language: str
    original_text: str
    translated_text: str
    processing_time: float