from django.db import models

# Create your models here.

class Images(models.Model):
    imageName = models.CharField(max_length=30)