from abc import ABC, abstractmethod


class BaseCleaner(ABC):
    """a base class for cleaner"""

    @abstractmethod
    def clean(self, text: str) -> str:
        raise NotImplementedError
