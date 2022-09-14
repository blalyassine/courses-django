from django.db import models
from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver


# //***  signal  for user
@receiver(post_save,sender=User)
def createProfile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create( user=instance,name=instance.username)
    else:
        profile=instance.profile
        profile.name=f"{instance.first_name.title()}{instance.last_name.upper()}"
        profile.save()
    
# post_save.connect(createProfile,sender=User) this function replace @receiver

@receiver(post_delete,sender=Profile)
def deleteUser(sender,instance,**kwargs):
    user=instance.user
    
    if not user.is_staff:
        user.delete()
    
# post_delete.connect(deleteUser,sender=Profile) this function replace @receiver 


