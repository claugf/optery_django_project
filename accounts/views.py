from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib import messages
from .forms import CreateUserForm


def index(request):
    return render(request, 'accounts/index.html')


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(
                request, 'You have been registered sucessfully, please Log In!')
            return redirect('accounts:login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('social:posts')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, 'You are logged out!')
    return redirect('accounts:login')


@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {'user': user}
    return render(request, 'accounts/user_profile.html', context)


def unauthorizedpage(request, exception):
    return render(request, 'accounts/403_csrf.html')


def notfoundpage(request, exception):
    return render(request, 'accounts/404code.html')


def errorpage(request):
    return render(request, 'accounts/500code.html')
