from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, LoginForm, UserProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DeletedAccountLog

# Home page (guide)
def index(request):
    return render(request, 'blog/index.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users1:login')
    else:
        form = UserCreationForm()
    return render(request, 'users1/signup.html', {'form': form})

# login page
def user_login(request):
    next_page = request.GET.get('next', 'starting-page')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(next_page)
    else:
        form = LoginForm()
    return render(request, 'users1/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('starting-page')

@login_required
def edit_account(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.users1_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Account updated successfully.")
            return redirect('users1:profile')
    else:
        form = UserProfileUpdateForm(instance=request.user.users1_profile)
    return render(request, 'users1/profile.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        profile = request.user.users1_profile
        profile.is_deleted = True
        profile.save()
        DeletedAccountLog.objects.create(user_id=request.user.id)
        logout(request)
        messages.info(request, "Your account has been marked as deleted.")
        return redirect('starting-page')
    return render(request, 'users1/profile.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.users1_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
    else:
        form = UserProfileUpdateForm(instance=request.user.users1_profile)
    return render(request, 'users1/profile.html', {'form': form})    

from .models import UserProfile  # Import the UserProfile model

@login_required
def user_profile(request):
    try:
        profile = request.user.users1_profile
    except UserProfile.DoesNotExist:
        return redirect('some_view_to_handle_missing_profile')
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.users1_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = UserProfileUpdateForm(instance=request.user.users1_profile)
    return render(request, 'users1/profile.html', {'form': form})


@login_required
def update_user_profile(request):
    if not request.user.is_superuser:
        if request.method == 'POST':
            form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.users1_profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully.')
                return redirect('profile')
        else:
            form = UserProfileUpdateForm(instance=request.user.users1_profile)
    else:
        messages.error(request, 'Superusers cannot use this form.')
        form = None
    return render(request, 'users1/profile.html', {'form': form})
