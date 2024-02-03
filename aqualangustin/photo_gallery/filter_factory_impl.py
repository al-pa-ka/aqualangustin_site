from core.filter import Filter
from core.filter_factory import FilterFactory
from .filter_impl import FilterImpl


class FilterFactoryImpl(FilterFactory):
    FILTERS = [
        #TODO
    ]

    def build(self, filter: dict[str, str]) -> Filter:
        alias_name, value = filter.items()[0]
        return self.FILTERS[alias_name](value)
