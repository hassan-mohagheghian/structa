from abc import ABC, abstractmethod


class Paradigm(ABC):
    name: str

    @abstractmethod
    def description(self) -> str:
        pass
