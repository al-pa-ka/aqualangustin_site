from abc import ABC, abstractmethod


class FilterQuery(ABC):
    @abstractmethod
    def get_query(self) -> dict[str, str]: ...
    