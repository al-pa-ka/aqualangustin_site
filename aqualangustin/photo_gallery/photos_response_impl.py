import json

from core.photo import Photo
from core.photos_response import PhotosResponse


class PhotosResponseImpl(PhotosResponse):
    def create_response(self, photos: list[Photo]) -> str:
        json.dumps([photo.get_serialized_data() for photo in photos])
        