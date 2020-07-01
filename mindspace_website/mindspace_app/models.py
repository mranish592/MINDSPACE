from django.db import models
from django.urls import reverse

# Create your models here.
class Activity(models.Model):
    heading = models.CharField(max_length=100)
    status = models.IntegerField()

    def __str__(self):
        return self.heading

    def get_absolute_url(self):
        return reverse("mindspace_app:index")
