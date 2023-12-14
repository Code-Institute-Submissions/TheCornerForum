from django.urls import path
from . import views

app_name = 'users1'

urlpatterns = [
    path("", views.StartingPageView.as_view(), namespace="starting-page"),
    path('login/', views.user_login, namespace='login'),
    path('signup/', views.user_signup, namespace='signup'),
    path('logout/', views.user_logout, namespace='logout'),
]


# blog urls.py
# urlpatterns = [
#     path("", views.StartingPageView.as_view(),
#          name="starting-page"),  # /starting-page
#     path("posts", views.AllPostsView.as_view(), name="posts-page"),  # /posts
#     path("posts/<slug:slug>", views.SinglePostView.as_view(),
#          name="post-detail-page"),  # /posts/my-first-post
#     path("read-later", views.ReadLaterView.as_view(), name="read-later"),

# ]
