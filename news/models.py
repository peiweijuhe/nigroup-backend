from django.db import models


# Create your models here.
class News(models.Model):
    link = models.CharField(max_length=128)
    date = models.CharField(max_length=128)
    content = models.TextField()


    def _str_(self):
        return self.content