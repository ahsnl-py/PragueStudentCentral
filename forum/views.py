from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Department, Subject, Notif_User, UploadFiles
from .forms import NewPost, NewPostUploads, NotifUser
from django.http import HttpResponse

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

# # Department View
def departments(request):
    departments = Department.objects.all()
    return render(request, 'forum/department.html', {'departments': departments})


# Subject and post view
def single_slug(request, single_slug):
    departments = [d.department_slug for d in Department.objects.all()]
    object_list = Post.published.all()
    
    # list all the subjects by department 
    if single_slug in departments:
        matching_subjects = Subject.objects.filter(department_name__department_slug=single_slug)
        
        subject_urls = {}
        for m in matching_subjects.all():
            try:
                part_one = object_list.filter(subject_name__subject_name=m.subject_name).earliest('publish')
                subject_urls[m] = part_one.slug
            except Exception: 
                pass
        context = {'m': matching_subjects, "part_ones": subject_urls}
        print(context)
        return render(request, "forum/subjects_by_department.html", context)

    # list all the post by the subject 
    post = [p.slug for p in object_list]
    if single_slug in post:
        posts = get_object_or_404(Post, slug=single_slug)
        post_from_subjects = Post.published.filter(subject_name__subject_name=posts.subject_name)
        this_post_idx = list(post_from_subjects).index(posts)

        context = {
            'post': posts
            ,'list_post_subjects': post_from_subjects 
            ,'this_post_idx': this_post_idx
        } 
        print(context)
        return render(request, 'forum/discussion.html', context)

    return HttpResponse(f"'{single_slug}' is not registesred!'")

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