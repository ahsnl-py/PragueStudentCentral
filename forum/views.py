from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    #print (request)
    return render(request, 'forum/home.html', context)

def about(request):
    print (request)
    return render(request, 'forum/about.html')