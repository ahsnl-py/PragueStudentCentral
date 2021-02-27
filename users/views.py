from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .forms import UserRegisterForm, UserProfileForm, UserForm
from .models import UserProfile
from forum.models import Post
from django.contrib.auth.models import User
from django.utils import timezone
from django.views.generic import (
    CreateView, DetailView, UpdateView, DeleteView, ListView, #FormView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def register(request):
    profile_form = UserProfileForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            pf = profile_form.save(commit=False)
            f.save()
            user = User.objects.get(id=f.id)
            pf.user = user
            pf.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            # return redirect('forum:forum-home')
            return redirect('update_profile', pk=f.id, username=f.username)
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def profile(request, pk, username):
    user = request.user
    print(username)
    user_info = User.objects.get(id=pk)
    user_profile = UserProfile.objects.get(user=pk)
    posts = Post.objects.filter(author=user_info.id)
    print(user_profile.user_picture)
    number_of_posts = len(posts)
    posts = posts[:5]
    context = {'user': user,
                'user_info': user_info,
                'user_profile': user_profile, 
                'posts': posts, 
                'number_of_posts': number_of_posts,}
    return render(request, 'users/profile.html', context)

class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url= "/login/"
    template_name = 'users/profile_update.html'
    model = User
    form_class = UserForm
    second_form_class = UserProfileForm

    def test_func(self):
        profile = self.get_object()
        if str(self.request.user) == str(profile.username):
            return True
        print(str(profile.username)== str(self.request.user))
        return False

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        user = UserProfile.objects.get(user=self.request.user.id)
        context['form2'] = self.second_form_class(instance = user)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = UserProfile.objects.get(user=request.user.id)
        form = self.form_class(request.POST, instance = request.user)
        form2 = self.second_form_class(request.POST, request.FILES, instance = user)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return redirect('profile', request.user.id, request.user)
        else:
            return self.render_to_response(
              self.get_context_data(form2=form2))
    

class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url= "/login/"
    template_name = 'users/delete_profile.html'
    model = User
    context_object_name = 'user'
    success_url = '/'

    def test_func(self):
        user = self.get_object()
        if str(self.request.user) == str(user.username):
            return True
        return False

# """ OLD CODE """
# def profile_edit(request, pk, username):
#     user = request.user
#     profile_form = UserProfileForm()
#     user_form = UserForm()
#     if request.method == 'POST':
#         profile_form = UserProfileForm(request.POST, request.FILES)
#         user_form = UserForm(request.POST)
#         if profile_form.is_valid() and user_form.is_valid():
#             user_info = User.objects.get(pk=user.id)
#             user_form = UserForm(request.POST, instance = user_info)

#             profile_info = UserProfile.objects.get(user=user)
#             profile_form = UserForm(request.POST, instance = user_info)
#             # profile = profile_form.save(commit=False)
#             # profile.user = user
#             profile_form.save()
#             # user_details = user_form.save(commit=False)
#             # user_details = user
#             user_form.save()
#             return redirect('/')
#         else:
#             print("Error")
#     return render(request, 'users/profile_update.html', {'user': user,
#                                                         'profile_form': profile_form,
#                                                         'user_form': user_form})


# class ProfileCreateView(LoginRequiredMixin, CreateView):
#     login_url= "/login/"
#     template_name = 'users/profile_update.html'
#     model = User
#     fields =  ['username','first_name']
#     context_object_name = 'form'

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)