from core.photo import Photo
from core.photo_storage import PhotoGetter
from core.filter_query import FilterQuery
from .models import Photo as PhotoModel


class PhotosGetterImpl(PhotoGetter):

    def get_photos(self, filters_query: FilterQuery) -> list[Photo]:
        django_represented_query = filters_query.get_query()
        django_model_photos = PhotoModel.objects.filter(**django_represented_query)
        photos: list[Photo] = [Photo(model) for model in django_model_photos]
        return photos