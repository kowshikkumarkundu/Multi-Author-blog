from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm,LoginForm


def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful.")
            return redirect("login")

    else:
        form = RegisterForm()
        

    return render(request, "accounts/register.html", {"form": form})


def login_user(request):

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                messages.success(request, "Login Successful.")
                return redirect("after_login")

    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})

@login_required
def after_login(request):
    return render(
        request,
        'user_home.html'
    )