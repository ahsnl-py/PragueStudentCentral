from django.db import models
from django.utils import timezone
from django.utils.text import slugify 
from django.contrib.auth.models import User
from django.urls import reverse 
from django.core.validators import MaxValueValidator, MinValueValidator


#Department Model
class Department(models.Model):
    department_name = models.CharField(max_length=255, unique=True)
    department_slug = models.CharField(max_length=255)
    no_subject = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], null=True)
    dept_code = models.IntegerField(null=True)

    class Meta:
        ordering = ('department_name',)

    def __str__(self):
        return self.department_name 

    def get_absolute_url(self):
        return reverse('forum:subject', kwargs={"dept_id" : self.id})

#Course or Subject Model
class Subject(models.Model):
    subject_name = models.CharField(max_length=250)
    subject_slug = models.CharField(max_length=250)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE, default=True)

    def __str__(self):
        return self.subject_name

    def get_absolute_url(self):
        return reverse('forum:post_by_subject', args=[self.department_name_id, self.id])


#Post manager -- Filter out views only by published post 
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

#Post model 
class Post(models.Model):
    
    # Status of user post publications:
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    #Models
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='posts', default=1)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') 
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now) 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='draft')

    #PublishManager -- filter only published article
    objects = models.Manager() #default manager
    published = PublishedManager() #Custome manager 
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta: 
        ordering = ('-publish',) 

    def __str__(self): 
        return self.title

    def get_absolute_url(self):
        return reverse('forum:post_detail', args=[self.pk, self.slug])

class UploadFiles(models.Model):
    file_upload = models.FileField(null=True, blank=True, upload_to='post_images/',)
    feed = models.ForeignKey(Post, on_delete=models.CASCADE)

class Notif_User(models.Model):
    user_email = models.EmailField(max_length=100, unique = True)
    time = models.DateTimeField(default=timezone.now)
    
    def __str__(self): 
        return self.user_email