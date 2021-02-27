from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User
from forum.models import Department

# Create your models here.
class UserProfile(models.Model):

    STATUS_CHOICES = (
            ('student', 'Student'),
            ('graduate', 'Graduate'),
            ( 'future student', 'Future Student')
        )

    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    user_department = models.CharField(max_length=250, blank = True)
    # user_department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank = True)
    user_picture = models.ImageField(null=True, blank=True, upload_to='post_images/',)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,null=True, blank=True,)

    
    # def __str__(self): 
    #     return self.user

    def get_absolute_url(self):
        return reverse('profile',
                        args=[self.user.pk, self.user])

    # def get_profile_picture(self):
    #     if self.user_picture
    #         return user_picture_url
    #     else:
    #         return 'your_default_img_url_path'
