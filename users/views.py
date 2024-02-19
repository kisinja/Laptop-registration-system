from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render


# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
    
            login(request, user)
            return redirect("home")
    return render(request, "accounts/login.html")


@login_required(login_url="/users/login/")
def user_logout(request):
    logout(request)
    return redirect("login")