from django.db import models


# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(null=True, blank=True, upload_to="img/gallery")
    key = models.CharField(max_length=128)


    def _str_(self):
        return self.title