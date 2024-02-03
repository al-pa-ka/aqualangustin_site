from ..core.photo import Photo
from .models import Photo as PhotoModel
from .serializers import PhotoSerializer


class PhotoImpl(Photo):
    def __init__(self, photo_model: PhotoModel) -> None:
        self.model = photo_model

    def get_serialized_data(self) -> dict:
        model_data: dict = PhotoSerializer(self.model).data
        return model_data
