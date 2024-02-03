from abc import ABC, abstractmethod


class Filter(ABC):
    @abstractmethod
    def get_django_representation(self) -> dict[str, str]: ...
