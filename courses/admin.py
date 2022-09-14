from django.contrib import admin
from .models import Course,Category,Tag
# Register your models here.

#m1
#admin.site.register(Course)

# admin.site.register([Course,Category,Tag])
@admin.register(Tag)
class Tagdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # pass
    search_fields = ("label","slug",)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # pass
    list_display=(
        "title",
        "slug",
        "publisherd",
        "instructor",
        "image",
        "price",
        "price_mad",
        "updated_at"
    )
    list_editable =( "publisherd","instructor", "title",)
    #** pour afecter lien 
    list_display_links = ("slug",)
    #** pour utilier recheche (admin)
    search_fields = ("title","slug",)
    #** pour utiliser filtter
    list_filter= ("title","instructor", "publisherd",)
    filter_horizontal = ("tags",) #**! this option selemnt [many to many]
    autocomplete_fields= ("instructor","category",)
    #**** paginaton
    list_per_page=1
    #** cette methed read only ne change pas
    # readonly_fields = ("slug","id") 
    # readonly_fields = ("id")
    # !!!! cette  methed utiliser pour les change ne pas readoly !!!!
    prepopulated_fields={ "slug": ("title","price")}
  
    
    

