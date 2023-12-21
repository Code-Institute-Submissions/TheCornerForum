from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path('all-posts/', views.AllPostsView.as_view(), name='all-posts-page'),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    path("cartoons/", views.CartoonView.as_view(), name="cartoons-page"),
    path("cartoons/<slug:slug>/", views.CartoonDetailView.as_view(), name="cartoon_detail"),
]
