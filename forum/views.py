from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Ahsnl7',
        'title': 'How to get bitches',
        'content': 'Be good looking',
        'date_posted': '12/01/2020',
    },
    {
        'author': 'Mike',
        'title': 'How to get good wife',
        'content': 'Be good citizen',
        'date_posted': '13/01/2020',
    }
]

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