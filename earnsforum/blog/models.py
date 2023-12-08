from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=175)
    excerpt = models.CharField(max_length=200, null=True, blank=True)
    image_name = models.CharField(max_length=120, null=True, blank=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(max_length=10000, null=True, blank=True)
