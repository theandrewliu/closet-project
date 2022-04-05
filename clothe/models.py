from django.db import models
from django.conf import settings
from section.models import Section

USER_MODEL = settings.AUTH_USER_MODEL
# Create your models here.


class Clothe(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField(null = True, blank = True)
    is_laundry = models.BooleanField(default=False)
    section = models.ForeignKey(
        Section, related_name="clothe", on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        USER_MODEL,
        null=True,
        related_name="clothe",
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name
