from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    user_department = models.CharField(max_length=250, blank = True)
    user_picture = models.ImageField(null=True, blank=True, upload_to='post_images/',)
    
    def __str__(self): 
        return self.user
