from django.db import models


# Create your models here.
class Publication(models.Model):
    author = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    link = models.CharField(max_length=128)
    press = models.CharField(max_length=128)
    issue = models.CharField(max_length=128)
    year = models.CharField(max_length=128)


    def _str_(self):
        return self.content