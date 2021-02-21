from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserProfileForm, UserForm
from .models import UserProfile
from forum.models import Post
from django.contrib.auth.models import User
from django.utils import timezone


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
            messages.success(request, f'Account created for {username}!')
            return redirect('forum:forum-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def profile(request):
    user = request.user
    user_profile = UserProfile()
    posts = Post.objects.filter(author=user)
    number_of_posts = len(posts)
    posts = posts[:5]
    context = {'user': user, 
                'user_profile': user_profile, 
                'posts': posts, 
                'number_of_posts': number_of_posts,}
    return render(request, 'users/profile.html', context)

def profile_edit(request):
    user = request.user
    profile_form = UserProfileForm()
    user_form = UserForm()
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES)
        user_form = UserForm(request.POST)
        if profile_form.is_valid() and user_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            user_details = user_form.save(commit=False)
            user_details = user
            user_details.save()
            return redirect('profile.html')
        else:
            print("Error")
    return render(request, 'users/edit_profile.html', {'user': user,
                                                        'profile_form': profile_form,
                                                        'user_form': user_form})