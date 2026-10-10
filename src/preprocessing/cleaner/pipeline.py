from .base import BaseCleaner
from .control import ControlCharCleaner
from .line_ending import LineEndingCleaner
from .null import NullCleaner
from .unicode import UnicodeCleaner


class CleanerPipeline(BaseCleaner):
    def __init__(self):
        self.cleaners: list[BaseCleaner] = [
            LineEndingCleaner(),
            ControlCharCleaner(),
            NullCleaner(),
            UnicodeCleaner()
        ]

    def clean(self, text: str) -> str:
        for cleaner in self.cleaners:
            text = cleaner.clean(text)
        return text
