
from django.urls import path
from .views import create,edit,delete,contact,list_courses,get_on_courses


urlpatterns = [
        path('', list_courses,name="courses_list"),
        path('<str:id>/',get_on_courses,name="courses_show"),
        path('create/',create,name="courses_create"),
        path('<str:id>/edit/',edit,name="courses_edit"),
        path('<str:pk>/delete/',delete,name="courses_delete"),
        
        path('contact/',contact,name="contact"),
        
        
]
