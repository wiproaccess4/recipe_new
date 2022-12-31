from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .models import MyUser


def registration(request):
    if request.method == "GET":
        return render(request, "authentication/registration.html")
    MyUser.objects.create_user(username=request.POST["username"],
                             email=request.POST["email"],
                             password=request.POST["password"])
    return HttpResponseRedirect("/")


def login_view(request):
    if request.method == "GET":
        return render(request, "authentication/login.html")

    user = authenticate(username=request.POST["username"], password=request.POST["password"])
    if user is not None:
        # request.session.create()
        login(request, user)
        print(request.session.session_key)
        request.session["user_name"] = request.user.username
        request.session["email"] = request.user.email
        return HttpResponseRedirect("/recipe/info/")
    return render(request, "authentication/login.html", {"error": "Invalid Credentials"})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
