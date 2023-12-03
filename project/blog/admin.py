from django.contrib import admin
from .models import TagModel,PostModel,AuthorModel,Comment
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_filter = ('caption',)

class PostAdmin(admin.ModelAdmin):
    list_filter = ('title','author')
    prepopulated_fields = {"slug":("title",)}

class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('first_name',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user_name','text']

admin.site.register(TagModel,TagAdmin)
admin.site.register(PostModel,PostAdmin)
admin.site.register(AuthorModel,AuthorAdmin)
admin.site.register(Comment,CommentAdmin)