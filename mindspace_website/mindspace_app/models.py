from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator




# Create your models here.
class Activity(models.Model):
    heading = models.CharField(max_length=100)
    #status = models.IntegerField()

    class Status(models.TextChoices):
        NEW = 'new', _('new')
        CURRENT = 'current', _('current')
        COMPLETED = 'completed', _('completed')

    status=models.CharField(
        max_length=100,
        choices=Status.choices,
        default=Status.NEW,
    )

    percentage= models.IntegerField(
        default = 0,
        validators=[MaxValueValidator(100), MinValueValidator(0)]
     )

    description = models.TextField(
        default = ' ',
        max_length=500,
    )

    def __str__(self):
        return self.heading

    def get_absolute_url(self):
        return reverse("mindspace_app:index")
