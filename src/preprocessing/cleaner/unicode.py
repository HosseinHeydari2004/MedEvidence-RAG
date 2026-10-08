from .base import BaseCleaner
import unicodedata

class UnicodeCleaner(BaseCleaner):

    def clean(self, text: str) -> str:
        text = unicodedata.normalize("NFKC", text)
        return text