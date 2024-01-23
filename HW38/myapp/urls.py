from django.urls import path
from .views import upload_image_and_create_thumbnail

urlpatterns = [
    path('', upload_image_and_create_thumbnail, name='upload_image'),
]