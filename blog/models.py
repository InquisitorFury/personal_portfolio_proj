from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.DateField(auto_now=False)
    images = models.ImageField(upload_to='blogs/images/', )