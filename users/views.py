from contextlib import redirect_stderr
from django.shortcuts import render,redirect
from .forms import SignupForm
from django.contrib.auth import login
# Create your views here.

def signup(request):
    
    if request.method== "POST" :
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect("/courses")
    else:
        form=SignupForm()
        
    return render(request,"registration/signup.html",{'form':form})