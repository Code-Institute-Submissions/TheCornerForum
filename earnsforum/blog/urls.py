from django.urls import path
from . import views
from .views import edit_comment, delete_comment, save_post


app_name = 'blog'

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts/", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    path("cartoons/", views.CartoonView.as_view(), name="cartoons-page"),
    path("cartoons/<slug:slug>/", views.CartoonDetailView.as_view(), name="cartoon_detail"),
    path('add_comment_to_post/<int:comment_id>/', views.add_comment_to_post, name='add_comment_to_post'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('save_post/<int:post_id>/', views.save_post, name='save_post'),
]
