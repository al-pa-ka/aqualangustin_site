from abc import ABC, abstractmethod
from .photo import Photo, PhotoData
from .filter_query import FilterQuery


class PhotoGetter(ABC):
    @abstractmethod
    def get_photos(self, filter_query: list[FilterQuery]) -> list[Photo]: ...


class PhotoSaver(ABC):
    @abstractmethod
    def add_photos(self, photos: list[PhotoData]): ...
