from django.db import models
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL

# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ManyToManyField(
        USER_MODEL,
        related_name="section"
    )
    
    def __str__(self):
        return self.name