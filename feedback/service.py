from typing import Protocol
from abc import abstractmethod

from better_profanity import profanity


class ICensorService(Protocol):
    @abstractmethod
    def has_profane(self, sentence: str) -> bool:
        raise NotImplementedError


class CensorService(ICensorService):
    def has_profane(self, text: str) -> bool:
        profanity.load_censor_words()
        profanity.add_censor_words(["welcome"])

        return profanity.contains_profanity(text)
