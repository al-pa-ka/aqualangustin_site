from abc import ABC, abstractmethod
from .filter import Filter


class FilterFactory(ABC):
    @abstractmethod
    def build(self, filter: dict[str, str]) -> Filter: ...
