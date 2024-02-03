from rest_framework.request import Request

from core.filter_query import FilterQuery
from core.get_request import GetRequestWithFilters
from .filter_factory_impl import FilterFactoryImpl
from .filter_query_impl import FilterQueryImpl


class GetRequestWithFiltersImpl(GetRequestWithFilters):
    def __init__(self, request: Request) -> None:
        self.request = request

    def get_filters(self) -> FilterQuery:
        try:
            filter_factory = FilterFactoryImpl()
            filters = self.request.data["filters"].items()
            query = [
                filter_factory.build({alias_filter_name: value})
                for alias_filter_name, value in filters
            ]
            return query
        except KeyError:
            return FilterQueryImpl([])
