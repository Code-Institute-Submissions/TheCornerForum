from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from users1.models import UserProfile

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
    image = models.ImageField(null=True, blank=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(max_length=10000, null=True, blank=True)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True)
    date = models.DateField(auto_now=True)
    text = models.TextField(max_length=2000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"{self.user.username} - {self.post.title}"

class Cartoon(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True)
    date = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

class CartoonPanel(models.Model):
    cartoon = models.ForeignKey(Cartoon, on_delete=models.CASCADE, related_name='panels')
    image = models.ImageField(upload_to='cartoons')
    caption = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.cartoon.title} Panel {self.order}"
    

class SavedContent(models.Model):
    user_profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='saved_content'
    )
    posts = models.ManyToManyField('Post', related_name='saved_by_users')
    cartoons = models.ManyToManyField('Cartoon', related_name='saved_by_users')

    def __str__(self):
        return f"SavedContent for {self.user_profile.user.username}"
      