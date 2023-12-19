from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm



#Home page (guide)
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
    next_page = request.GET.get('next') or request.POST.get('next') or 'starting-page'

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

# logout page
def user_logout(request):
    logout(request)
    return redirect('starting-page')