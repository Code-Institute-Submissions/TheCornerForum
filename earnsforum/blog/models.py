from django.db import models


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()



class Post(models.Model):
    title = models.CharField(max_length=175)
    excerpt = models.CharField(max_length=200, null=True, blank=True)
    image_name = models.CharField(max_length=120, null=True, blank=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(max_length=10000, null=True, blank=True)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True)
