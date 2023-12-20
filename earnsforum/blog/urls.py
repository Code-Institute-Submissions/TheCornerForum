from django.urls import path
from . import views
from .views import posts, edit_comment, delete_comment, save_post


app_name = 'blog'

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts/", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    path("cartoons/", views.CartoonView.as_view(), name="cartoons-page"),
    path("cartoons/<slug:slug>/", views.CartoonDetailView.as_view(), name="cartoon_detail"),
    path('edit_comment/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('delete_comment/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('save_post/<int:post_id>/', save_post, name='save_post'),
]
