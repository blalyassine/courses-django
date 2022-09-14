
from django import forms
from courses.models import Course



PROFITION = (
    ("Student","Student"),
    ("Devloper","Devloper"),
    ("Entrepreneur","Entrepreneur"),
    ("Teacher","Teacher"),
)

class ContactForm(forms.Form):
    profition=forms.ChoiceField(choices=PROFITION,widget=forms.Select(attrs={ "class":"form-control"}))
    name=forms.CharField(min_length=4,widget=forms.TextInput(attrs={ "class":"form-control"}))
    email=forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={ "class":"form-control"}))
    subject=forms.CharField(min_length=5,max_length=50,widget=forms.TextInput(attrs={ "class":"form-control"}))
    message=forms.CharField(widget=forms.Textarea(attrs={ "class":"form-control","rows":3 }))
    


class CoursesForm(forms.ModelForm):
    class Meta:
        model=Course
        # fields="__all__"  #afficher tous les chanps
        exclude=["publisherd"]  #afficher tous les chanps soff publisherd
        
    def __init__(self,*args, **kwargs) :
        super().__init__(*args, **kwargs)
        
        for (element,field) in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
        
        #afficher tous les chanps appeler dans fields
        # fields=[
        #     "publisherd",
        #     "title",
        #     "slug"
        #     "price",
        #     "images",
        #     'body',
        #     "instructor",
        #     "category",
        #     "tags",
        # ]
        
        # widgets={
        #      "title" : forms.TextInput(attrs={"class":"form-control"}),
        #     #  "email" : forms.EmailField(attrs={"class":"form-control"}),
        #      "slug" : forms.TextInput(attrs={"class":"form-control"}),
        #      "body" : forms.Textarea(attrs={"class":"form-control","rows":4}),
        #      "price" : forms.NumberInput(attrs={"class":"form-control"}),
        #      "images" : forms.URLInput(attrs={"class":"form-control"}),
        #      "instructor" : forms. Select(attrs={"class":"form-control"}),
        #      "category" : forms.Select(attrs={"class":"form-control"}),
        #      "tags" : forms.SelectMultiple(attrs={"class":"form-control"}),
        # }
        
