from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.views import View
from .forms import ContactForm ,CoursesForm
from django.contrib import messages
from .models import Course, Tag
from django.contrib.auth.decorators import login_required
# Create your views here.

# get_cours=[
#   {
#     "id":1,
#     "title": "django 4",
#     "body": "lorem ipsun lorem lorem lorem lorem lorem lorem lorem loremlorem lorem lorem lorem lorem",
#     "price":30,
#     "image":"https://process.fs.teachablecdn.com/ADNupMnWyR7kCWRvm76Laz/resize=width:705/https://file-uploads.teachablecdn.com/1a87c398761d4629a38126a31a8d93e1/eaa52d6815e44538bcc1068aca541ab7"

   
#   },
#   {
#     "id":2,
#     "title": "flask",
#     "image":"https://process.fs.teachablecdn.com/ADNupMnWyR7kCWRvm76Laz/resize=width:705/https://file-uploads.teachablecdn.com/1a87c398761d4629a38126a31a8d93e1/eaa52d6815e44538bcc1068aca541ab7",
#     "body": "lorem ipsun lorem lorem lorem lorem lorem lorem lorem loremlorem lorem lorem lorem lorem",
#     "price":20
    
#   },
#         {
#     "id":3,
#     "title": "laavel",
#     "image":"https://process.fs.teachablecdn.com/ADNupMnWyR7kCWRvm76Laz/resize=width:705/https://file-uploads.teachablecdn.com/1a87c398761d4629a38126a31a8d93e1/eaa52d6815e44538bcc1068aca541ab7",
#     "body":"<b>lorem ipsun<b> lorem lorem lorem lorem lorem lorem lorem loremlorem lorem lorem lorem lorem",
#     "price":0
    
#   },
# ]


def list_courses(request):
    title="cours app"
    body="lorem ipsun lorem lorem lorem lorem lorem lorem lorem loremlorem lorem lorem lorem lorem"
    
    get_cours=Course.objects.all()
    #data={"title":"cours app","body":"lorem ipsun"}
    return render(request,'courses/index.html',{"title" :title,"body" : body,"courses":get_cours})
    #return render(request,'courses/index.html',{"title"="cours app","body"="lorem ipsun"})
    #return render(request,'courses/index.html',context=data)
    #return render(context=data,template_name='courses/index.html',request=request)
  # return HttpResponse("<h1> list of courses</h1>")

def get_on_courses(request,id):
  # try:
  #   course=Course.objects.get(id=id)
  #   return render(request,'courses/show.html',{"course":course})
  #   #return HttpResponse(f"<h1>courses {id}</h1>")
  # except:
  #   raise Http404
  course=get_object_or_404(Course,pk=id)
  return render(request,'courses/show.html',{"course":course})
  
def contact(request):
  
  if request.method=="POST":
    form_contact=ContactForm(request.POST)
    if form_contact.is_valid():
      print(form_contact.cleaned_data)
  else:
    form_contact = ContactForm()
    
  return render(request,"courses/contact.html",{ "form": form_contact })

@login_required(login_url="/login")
def create(request):
    
  if request.method=="POST":
    form_create=CoursesForm(request.POST)
    if form_create.is_valid():
      form_create.save()
      return redirect("courses_list")
      # return HttpResponse("Course saved")
  else:
    form_create = CoursesForm()
    
  return render(request,"courses/create.html",{ "form": form_create })
  

def edit(request,id):
  
  course=Course.objects.get(pk=id)
  
  if request.method=="POST":
    form_edit=CoursesForm(request.POST, instance=course)
    if form_edit.is_valid():
      form_edit.save()
      return redirect("courses_show",id=id)
      # return HttpResponse("Course updated")
  else:
    form_edit = CoursesForm(instance=course)
    
  return render(request,"courses/edit.html",{ "form": form_edit })
  
  
def delete(request,id):
  course=Course.objects.get(pk=id)
  if request.method=="POST":
    course.delete()
    return redirect("courses_list")
    
    # return HttpResponse("Course deleted")
  
  return render(request,"courses/delete.html",{ "course": course })
