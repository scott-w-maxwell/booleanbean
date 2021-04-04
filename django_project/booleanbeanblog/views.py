from django.shortcuts import render
from django.http import HttpResponse


# Dummy data
posts = [
    {
        'author': 'Scott M',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '4-3-2021'
    },
    {
        'author': 'Scott M',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': '4-3-2021'
    }
]


def home(request):
    
    context = {
        'posts': posts
    }

    return render(request, 'home.html', context)