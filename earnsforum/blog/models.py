from django.db import models


class Tag(models.Model):
    caption = models.CharField(max_length=20)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()


class Post(models.Model):
    title = models.CharField(max_length=175)
    excerpt = models.CharField(max_length=200, null=True, blank=True)
    image_name = models.CharField(max_length=120, null=True, blank=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(max_length=10000, null=True, blank=True)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    tags = models.ManyToManyField(Tag)
