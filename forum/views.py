from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponse

# List of post 
def post_list(request):
    posts = Post.published.all()
    context = {
                'posts': posts
              }
    posts = Post.published.all()
    return render(request, 'forum/list.html', context)

# Detail post 
def post_detail(request, year, month, day, post):
    post = get_object_or_404(
                                Post, 
                                slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day,
                            )
    context = {'post': post}
    return render(request, 'forum/detail.html', context)

# Create your views here.
def home(request):
    #print (request)
    return render(request, 'forum/home.html')

def about(request):
    print (request)
    return render(request, 'forum/home2.html')