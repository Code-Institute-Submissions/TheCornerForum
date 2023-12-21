from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users1'

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('edit_account/', views.edit_account, name='edit_account'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('profile/', views.user_profile, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
]