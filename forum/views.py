from .models import Post, Department, Subject, Notif_User, UploadFiles
from .forms import NewPost, NewPostUploads, NotifUser

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView, DetailView, UpdateView, DeleteView, ListView, #FormView
)

# View home
def home(request):
    form = NotifUser
    if request.method == 'POST':
        form = NewPost(request.POST,)
        if form.is_valid():
            form.save()
            render(request, 'forum/home.html')
    else:
        print("** ERROR! **")
    return render(request, 'forum/home.html')

# About view
def about(request):
    return render(request, 'forum/about.html')

# Department View
def departments(request):
    departments = Department.objects.all()
    return render(request, 'forum/department.html', {'departments': departments})

# Subject View by Department 
def subject_dept(request, dept_id):
    all_dept_id = [d.id for d in Department.objects.all()]
    if dept_id in all_dept_id:
        match_subject_dept = Subject.objects.raw(
                                            ''' SELECT * 
                                                FROM forum_subject 
                                                WHERE department_name_id = %s 
                                            ''', [dept_id])
        list_subject_by_dept = []                                    
        for subject_dept_list in match_subject_dept:
            list_subject_by_dept.append(subject_dept_list)
            context = {'subject_list': list_subject_by_dept}
        
        return render(request, "forum/subjects_by_department.html", context)

    else:
        return HttpResponse('Department does not exists!')

# Post View by Subjects
def post_subject_dept(request, dept_id, subject_name_id):
    all_subject_dept_id = [s.department_name_id for s in Subject.objects.all()]
    if dept_id in all_subject_dept_id:
        match_post = Post.objects.raw(
                                ''' SELECT * 
                                    FROM forum_post 
                                    WHERE subject_name_id = %s 
                                ''', [subject_name_id])
        list_post_by_subject = []                                
        for post_list in match_post:
            list_post_by_subject.append(post_list)
            context = {'posts_by_subjects' : list_post_by_subject}
        
        return render(request, 'forum/discussion.html', context)
    else:
        return HttpResponse('Subject does not exists!')

# List of post 
def post_list(request):
    posts = Post.published.all()
    return render(request, 'forum/list.html', {'posts': posts})

class PostDetailView(DetailView):
    template_name = 'forum/detailed.html'
    model = Post

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'forum/delete_post.html'
    model = Post
    success_url = '/post/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostCreateView(LoginRequiredMixin, CreateView):
    login_url= "/login/"
    template_name = 'forum/new_post.html'
    model = Post
    form_class = NewPost
    second_form_class = NewPostUploads
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['form2'] = self.second_form_class()
        context['title'] = 'Create Post'
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST, request.FILES)
        files = request.FILES.getlist('file_upload')
        if form.is_valid() and form2.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.status = 'published'
            new_post.save()
            for f in files:
                file_instance = UploadFiles(file_upload=f, feed=new_post)
                file_instance.save()
            return redirect('forum:forum_post_list')
        else:
            return redirect('forum:new_post')

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url= "/login/"
    template_name = 'forum/new_post.html'
    model = Post
    form_class = NewPost
    second_form_class = NewPostUploads
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        post = self.get_object()
        context['form2'] = self.second_form_class(instance=post)
        context['title'] = 'Edit Post'
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = self.form_class(request.POST, instance=post)
        form2 = self.second_form_class(request.POST, request.FILES)
        files = request.FILES.getlist('file_upload')
        if form.is_valid() and form2.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.status = 'published'
            new_post.save()
            for f in files:
                file_instance = UploadFiles(file_upload=f, feed=new_post)
                file_instance.save()
            return redirect('forum:post_detail', post.id, post.slug)
        else:
            return redirect('forum:new_post')
    

