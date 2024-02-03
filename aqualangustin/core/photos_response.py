from .photo import Photo


class PhotosResponse:
    def create_response(self, photos: list[Photo]) -> str: ...
    