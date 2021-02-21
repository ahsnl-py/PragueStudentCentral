from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Department, Subject, Notif_User, UploadFiles
from .forms import NewPost, NewPostUploads, NotifUser
from django.http import HttpResponse
from django.views.generic import (
    #CreateView, 
    #DetailView, 
    #UpdateView, 
    #DeleteView,
    ListView
    #FormView
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
    files = UploadFiles.objects.filter(feed=post)
    context = {
        'post': post, 
        'files': files
    }
    return render(request, 'forum/detail.html', context)

"""Test detailed page"""
def TEST_post_detail(request, year, month, day, post):
    post = get_object_or_404(
                                Post, 
                                slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day,
    )
    files = UploadFiles.objects.filter(feed=post)
    context = {
        'post': post, 
        'files': files
    }
    return render(request, 'forum/detailed_2.html', context)

def new_post(request):
    form = NewPost()
    upload = NewPostUploads()
    if request.method == 'POST':
        form = NewPost(request.POST,)
        upload = NewPostUploads(request.POST, request.FILES)
        files = request.FILES.getlist('file_upload')
        if form.is_valid() and upload.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.status = 'published'
            new_post.save()
            for f in files:
                file_instance = UploadFiles(file_upload=f, feed=new_post)
                file_instance.save()
            return redirect('forum:forum_post_list')
        else:
            pass
    
    return render(request, 'forum/new_post.html', {'form':form, 'upload':upload})

""" OLD CODE """
# def subject_by_department(request, dept_slug):
#     print(request, dept_slug)
#     departments = [d.department_slug for d in Department.objects.all()]
#     # list all the subjects by department 
#     if dept_slug in departments:
#         matching_subjects = Subject.objects.filter(department_name__department_slug=dept_slug)
#         subject_urls = {}
#         for m in matching_subjects.all():
#             try:
#                 part_one = Post.published.all().filter(subject_name__subject_name=m.subject_name).earliest('publish')
#                 subject_urls[m] = part_one.slug
#             except Exception: 
#                 pass 

#         return render(request, "forum/subjects_by_department.html", {'subject_name': matching_subjects, "part_ones": subject_urls})    
    
    # post = [p.slug for p in Post.published.all()]
    # if dept_slug in post:
    #     posts = get_object_or_404(Post, slug=dept_slug)
    #     post_from_subjects = Post.published.filter(subject_name__subject_name=posts.subject_name)
        
    #     this_post_idx = list(post_from_subjects).index(posts)

    #     return render(request, 'forum/discussion.html', {'post': posts, 'list_post_subjects': post_from_subjects, 'this_post_idx': this_post_idx})

    # return HttpResponse(f"'{dept_slug}' is not registesred!'")

# Subject View
# class UserPostListView(ListView):
#     model = Subject
#     template_name = 'forum/subjects_by_department.html'
#     context_object_name = 'subjects'

#     def get(self, request):
#         matching_subjects = Subject.objects.filter(department_name__department_slug=single_slug)
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Post.published.filter(author=user).order_by('-publish')
