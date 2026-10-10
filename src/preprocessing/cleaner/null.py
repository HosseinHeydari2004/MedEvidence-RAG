from .base import BaseCleaner
import re


class NullCleaner(BaseCleaner):
    _NULL_RE: re.Pattern[str] = re.compile(r"\x00")
    _WS_RE: re.Pattern[str] = re.compile(r"[^\S\n]+")

    def clean(self, text) -> str:
        if not text or "\x00" not in text:
            return text

        text = self._NULL_RE.sub(" ", text)
        text = self._WS_RE.sub(" ", text)
        return text
