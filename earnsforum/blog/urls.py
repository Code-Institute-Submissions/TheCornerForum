from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts/", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page"),
    #path("posts/<slug:slug>/comment/", views.AddCommentView.as_view(), name="add-comment"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),

]
