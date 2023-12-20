from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, LoginForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.utils import timezone
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
    return render(request, 'signup.html', {'form': form})

# login page


def user_login(request):
    next_page = request.GET.get('next') or request.POST.get(
        'next') or 'starting-page'

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(next_page)
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'next': next_page})


@login_required
def user_logout(request):
    logout(request)
    return redirect('starting-page')


def edit_account(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # Redirect to a success page or profile page
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'users1/edit_account.html', {'form': form})


@login_required
def delete_account(request):
    if request.method == 'POST':

        profile = request.user.users1_profile
        profile.is_deleted = True
        profile.deleted_at = timezone.now()
        profile.save()

        # Log the deletion
        DeletedAccountLog.objects.create(
            user_id=request.user.id, deletion_date=timezone.now())

        # Anonymize or modify other user data as necessary
        # request.user.email = 'anonymized@example.com'
        # request.user.username = 'anonymized_user_' + str(request.user.id)
        # request.user.save()

        logout(request)
        messages.info(request, "Your account has been marked as deleted.")
        # Replace 'home' with the name of your home page URL
        return redirect('home')

    return render(request, 'users1/delete_account.html')
