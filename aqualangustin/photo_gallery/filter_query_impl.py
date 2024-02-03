from core.filter import Filter
from core.filter_query import FilterQuery


class FilterQueryImpl(FilterQuery):
    def __init__(self, filters: list[Filter]) -> None:
        self.query = filters

    def get_query(self) -> dict[str, str]:
        filters = {}
        for filter in self.query:
            filters |= filter
        return filters