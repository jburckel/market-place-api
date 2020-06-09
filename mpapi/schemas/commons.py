from pydantic import BaseModel
from typing import Optional

class MultiLanguageText(BaseModel):
    en: str = None
    es: str = None
    fr: str = None

class Image(BaseModel):
    url: str
    name: MultiLanguageText
