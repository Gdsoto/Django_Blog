from django.shortcuts import render
from blog.models import Post

# Create your views here.

def posts(request):

    posts = Post.objects.filter(public=True).all()

    return render(request, 'post/posts.html', {
        'title': 'All Posts',
        'posts': posts
    })
