from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

# Create your views here.

def create_thumbnail(uploaded_file, thumbnail_size=(50, 50)):
    image = Image.open(uploaded_file)
    image.thumbnail(thumbnail_size)
    thumbnail_io = BytesIO()
    image.format = 'JPEG'
    image.save(thumbnail_io, format=image.format, quality=85)
    thumbnail_io.seek(0)
    thumbnail_name = f'thumbnails/{uploaded_file.name.split(".")[0]}_thumbnail.jpg'
    thumbnail_file = ContentFile(thumbnail_io.getvalue(), name=thumbnail_name)
    thumbnail_path = default_storage.save(thumbnail_name, thumbnail_file)
    return default_storage.url(thumbnail_path)

def upload_image_and_create_thumbnail(request):
    if request.method == 'POST' and request.FILES['image']:
        uploaded_file = request.FILES['image']
        thumbnail_url = create_thumbnail(uploaded_file)
        return HttpResponse(f'Thumbnail URL: {thumbnail_url}')
    else:
        return render(request, 'index.html')