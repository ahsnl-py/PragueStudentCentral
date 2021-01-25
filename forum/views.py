from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post, Department, Subject
from django.http import HttpResponse

# Department View
def departments(request):
    departments = Department.objects.all()
    return render(request, 'forum/department.html', {'departments': departments})

# Subject and post view
def single_slug(request, single_slug):
    print(single_slug) 
    departments = [d.department_slug for d in Department.objects.all()]
    object_list = Post.published.all()
    
    # list all the subjects by department 
    if single_slug in departments:
        matching_subjects = Subject.objects.filter(department_name__department_slug=single_slug)
        print(matching_subjects)
        
        subject_urls = {}
        for m in matching_subjects.all():
            try:
                part_one = object_list.filter(subject_name__subject_name=m.subject_name).earliest('publish')
                subject_urls[m] = part_one.slug
            except Exception: 
                pass 

        return render(request, "forum/subjects_by_department.html", {'m': matching_subjects, "part_ones": subject_urls})

    # list all the post by the subject 
    post = [p.slug for p in object_list]
    if single_slug in post:
        posts = get_object_or_404(Post, slug=single_slug)
        post_from_subjects = Post.published.filter(subject_name__subject_name=posts.subject_name)
        
        this_post_idx = list(post_from_subjects).index(posts)

        return render(request, 'forum/discussion.html', {'post': posts, 'list_post_subjects': post_from_subjects, 'this_post_idx': this_post_idx})

    return HttpResponse(f"'{single_slug}' is not registesred!'")

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
    print (request)
    return render(request, 'forum/home.html')

def about(request):
    print (request)
    return render(request, 'forum/about.html')

def forum(request):
    print (request)
    return render(request, 'forum/home3.html')

