from abc import ABC, abstractmethod
from .filter_query import FilterQuery


class GetRequestWithFilters(ABC):
    @abstractmethod
    def get_filters(self) -> FilterQuery: ...
