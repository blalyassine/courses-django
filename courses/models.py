from django.db import models
from django.utils.text import slugify
from users.models import Profile
from django.contrib.auth.models import User
import uuid


# Create your models here.

    
class Category(models.Model):
    label=models.CharField(max_length=30)
    slug=models.SlugField(max_length=40,editable=False)
    
    
    def __str__(self):
        return f"{self.label}({self.id})"
    
    # this methed or preadonly_fields 
    # def save(self,*args, **kwargs):
    
    #     if not self.slug:
            
    #         self.slug=slugify(self.label)
            
    #     super().save(*args, **kwargs)


class Tag(models.Model):
    label=models.CharField(max_length=20)
    
    def __str__(self):  
        return f"{self.label}({self.id})"

class Course(models.Model):
    tags=models.ManyToManyField(Tag)
    instructor=models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    # id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    title=models.CharField(max_length=100)
    body=models.TextField()
    image=models.URLField(null=True)
    price=models.FloatField()
    slug=models.SlugField( null=True,max_length=100,blank=True)
    publisherd=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}({self.id})"
    
    class Meta:
        # ordering=["updated_at"] # croissent
        # ordering=["-updated_at"] # decriscent
        ordering=["-updated_at","publisherd"] # decriscent & or
        
    @property
    def price_mad(self):
        return self.price*10
    
    @property
    def active(self):
        if self.publisherd:
            return "is publisherd"
        return "not publisherd"
    
    # cette methed est pused becauuse i use readonly_fields 
    # def save(self,*args, **kwargs):
        
    #     if not self.slug:
            
    #         self.slug=slugify(self.title)
            
    #     super().save(*args, **kwargs)