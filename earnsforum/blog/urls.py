from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"), # /starting-page
    path("posts", views.posts, name="posts-page"), # /posts
    path("posts/<slug:slug>", views.post_detail,
         name="post-detail-page"), # /posts/my-first-post
]