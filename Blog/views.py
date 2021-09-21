from django.shortcuts import render
from .models import Blog

# Create your views here.

def showBlog(request):
    blogs=Blog.objects.all()

    context={
        'blogs':blogs
    }
    return render(request, 'Blog/Blogs.html', context)