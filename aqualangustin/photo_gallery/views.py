import json

from django.shortcuts import render
from rest_framework.request import Request
from django.http.request import HttpRequest
from django.shortcuts import render

from .photo_getter_impl import PhotosGetterImpl
from .get_request_with_filters_impls import GetRequestWithFiltersImpl
from .photos_response_impl import PhotosResponseImpl
# Create your views here.


def get_photos(request: Request):
    filters = GetRequestWithFiltersImpl(request).get_filters()
    photos_getter = PhotosGetterImpl()
    photos = photos_getter.get_photos(filters)
    return PhotosResponseImpl().create_response(photos)

def index(request: Request):
    return render(request, 'index.html')

def hanlde_404(request: Request | HttpRequest, exception):
    print('handle 4040')
    print(request.get_full_path())
    print(request.get_full_path().count('/static/'))
    if request.get_full_path().count('/static/') == 0:
        return render(request, 'index.html')
