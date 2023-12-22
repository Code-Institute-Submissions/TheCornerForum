from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, LoginForm, UserProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DeletedAccountLog
from .models import UserProfile

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
                # Check if user profile is marked as deleted
                try:
                    if user.users1_profile.is_deleted:
                        messages.error(request, "This account has been deleted.")
                        return redirect('users1:login')
                except UserProfile.DoesNotExist:
                    # Handle case where UserProfile does not exist
                    pass

                login(request, user)
                return redirect(next_page)
            else:
                messages.error(request, "Invalid username or password.")
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
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        if created:
            # Handle the case where the profile didn't exist
            profile.is_deleted = True
            profile.save()

        # Marking the profile as deleted
        profile.is_deleted = True
        profile.save()

        # Log the deletion
        DeletedAccountLog.objects.create(user_id=request.user.id)

        # Log out the user
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


@login_required
def user_profile(request):
    # Get the user's existing profile or create a new one if it doesn't exist
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('users1:profile')
    else:
        form = UserProfileUpdateForm(instance=profile)

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
