from django.db import models


# Create your models here.


class SkinDisease(models.Model):
    name = models.CharField(max_length=255)
    disease_ar = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    symptoms = models.TextField()
    risk_factors = models.TextField()
    coping_with = models.TextField()
    advices = models.TextField()
    read_more = models.URLField(null=True, blank=True)
    model_class_num = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
