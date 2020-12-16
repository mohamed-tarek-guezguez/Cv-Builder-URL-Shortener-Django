from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db import models
from PIL import Image

# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, blank=True, null=True)
    tag = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    about = RichTextField(blank=True, null=True)
    skills = RichTextField(blank=True, null=True)
    experience = RichTextField(blank=True, null=True)
    education = RichTextField(blank=True, null=True)
    services = RichTextField(blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=250, blank=True, null=True)
    template = models.CharField(max_length=250, default='cv1.html')

    def __str__(self):
        return f'{self.user.username} Profile'
