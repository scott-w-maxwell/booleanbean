from django.shortcuts import render
from django.http import HttpResponse


from .models import Post

posts = Post.objects.all()


def home(request):
    
    context = {
        'posts': posts
    }

    return render(request, 'home.html', context)