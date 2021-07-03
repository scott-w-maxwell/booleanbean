from django.shortcuts import render
from django.http import HttpResponse


from .models import Post

# Retrieve from  db.sqlite database
posts = Post.objects.all()


def home(request):
    
    context = {
        'posts': posts
    }

    return render(request, 'home.html', context)

def about(request, *args, **kwargs):
    return render(request, 'about.html')