from datetime import timezone

from api.models import User
from django.db import models

from SkinDiseaseApp.models import SkinDisease


# Create your models here.


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class History(models.Model):
    skin_diseases = models.ForeignKey(SkinDisease, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.URLField(default="noImage")
    created_at = models.DateTimeField(auto_now_add=True )
    updated_at = models.DateTimeField(auto_now=True)



class ImageUpload(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image)
