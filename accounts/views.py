from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    # if user logged in redirect to home
    if not request.user.is_anonymous:
        return redirect("/")
    # form title
    title = "Login"
    # use user login form from forms
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        # get posted data of username and password
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        login(request,user)
        # redirect to home after logged in
        return redirect("/")
    context = {
        "form": form,
        "title": title,
    }
    return render(request, "accounts/login_form.html", context)

def register_view(request):
    # if user logged in redirect to home
    if not request.user.is_anonymous:
        return redirect("/")
    # form title
    title = "Register"
    # use user register form from forms
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        # automatically log in new user on registration
        new_user = authenticate(username=user.username,password=password)
        login(request, new_user)
        # redirect to home after user creation and logged in
        return redirect("/")
    context = {
        "form": form,
        "title": title,
    }
    return render(request, "accounts/register_form.html", context)

def logout_view(request):
    logout(request)
    # redirect to home after logged out
    return redirect("/")