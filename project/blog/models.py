from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class TagModel(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.caption}"


class AuthorModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.full_name()

class PostModel(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=150)
    img_name = models.ImageField(upload_to='posts',null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True,db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(AuthorModel,on_delete=models.SET_NULL,null=True,related_name="posts")
    tag = models.ManyToManyField(TagModel)

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(PostModel,on_delete=models.SET_NULL,null=True,related_name='comments')