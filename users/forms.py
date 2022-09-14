

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        # fields="__all__"
        fields=[
            "username",
            "email",
        ]