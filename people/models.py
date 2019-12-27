from django.db import models

TITLE_CHOICES = (
    ('Professor', 'Professor'),
    ('Associate Professor', 'Associate Professor'),
    ('Assistant Professor', 'Assistant Professor'),
    ('Postdoc Fellow', 'Postdoc Fellow'),
    ('Ph.D. Candidate', 'Ph.D. Candidate'),
    ('MPhil Candidate', 'MPhil Candidate'),
    ('Research Assistant', 'Research Assistant'),
    ('Alumni', 'Alumni'),
)


# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=128)
    title = models.CharField(choices=TITLE_CHOICES, max_length=128)
    email = models.CharField(max_length=128)
    project = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    experience = models.TextField()
    completed = models.BooleanField(default=False)
    headshot = models.ImageField(null=True, blank=True, upload_to="img/headshot")

    def _str_(self):
        return self.name
