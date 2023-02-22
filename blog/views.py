from django.shortcuts import render
from .models import blog
# Create your views here.
def all_blogs(request):
    articles = blog.objects.all()
    return render(request, 'blog/all_blogs.html', {'articles':articles})