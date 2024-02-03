from django.db import models

# Create your models here.

class Photo(models.Model):
    raw_photo = models.FileField(null=True, blank=True, upload_to='static/raws')
    non_compressed_photo = models.ImageField(upload_to='../static/non_compressed')
    photo_view = models.ImageField(upload_to='../stastic/images')
    title = models.CharField(null=True, blank=True, max_length=100)
    inscription = models.TextField(null=True, blank=True)
