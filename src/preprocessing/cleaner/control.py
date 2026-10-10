from .base import BaseCleaner
import re


class ControlCharCleaner(BaseCleaner):
    _CONTROL_RE = re.compile(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]")

    def clean(self, text: str) -> str:
        text = self._CONTROL_RE.sub("", text)
        return text
