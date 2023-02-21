from django.contrib import admin
from .models import Projects
# Register your models here.

# this will add the projects class into the admin site
# for the admin to change it
admin.site.register(Projects) 