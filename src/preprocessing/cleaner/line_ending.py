from .base import BaseCleaner
import re


class LineEndingCleaner(BaseCleaner):
    _LINE_ENDING_RE = re.compile(r"\r\n|\r")

    def clean(self, cls, *, text: str) -> str:
        text = cls._LINE_ENDING_RE.sub("\n", text)
