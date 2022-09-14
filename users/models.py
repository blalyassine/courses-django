# from distutils.command.upload import upload
# import profile
# from tkinter import CASCADE
# from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from uuid import uuid4

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=30,null=True)
    email=models.CharField(max_length=80,null=True)
    description=models.TextField(null=True)
    image=models.ImageField(null=True,upload_to='profile/')
    url=models.URLField(null=True)
    id=models.UUIDField(default=uuid4,unique=True,primary_key=True,editable=False)
    
    
    
    def __str__(self):
        #  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
         if self.user:
           return f'{self.user.username}'
        # /return f"{self.user.username}"
        
    # def __str__(self):
    #    return str(self.pressid)
