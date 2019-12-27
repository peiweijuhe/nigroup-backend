from django.db import models


# Create your models here.
class Research(models.Model):
    link = models.CharField(max_length=128)
    image = models.ImageField(null=True, blank=True, upload_to="img/research")
    title = models.CharField(max_length=128)
    content1 = models.TextField()
    content2 = models.TextField()
    content3 = models.TextField()


    def _str_(self):
        return self.title