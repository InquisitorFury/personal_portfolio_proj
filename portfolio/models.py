from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)