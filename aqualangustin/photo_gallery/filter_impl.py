from core.filter import Filter


class FilterImpl(Filter):
    def __init__(self, name: str, value: str) -> None:
        self.name = name
        self.value = value

    def get_django_representation(self) -> dict[str, str]:
        return {self.name: self.value}
    