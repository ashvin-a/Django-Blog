from django.contrib import admin
from .models import TagModel,PostModel,AuthorModel
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_filter = ('caption',)

class PostAdmin(admin.ModelAdmin):
    list_filter = ('title','author')
    prepopulated_fields = {"slug":("title",)}
    
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('first_name',)

admin.site.register(TagModel,TagAdmin)
admin.site.register(PostModel,PostAdmin)
admin.site.register(AuthorModel,AuthorAdmin)