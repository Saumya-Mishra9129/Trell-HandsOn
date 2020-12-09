# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import NewUserForm
from django.contrib.auth import authenticate, login,logout

# Create your views here.


def login_request(request):
    if request.method == "POST":
        form = NewUserForm()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}")
                return redirect('templates/dashboard/homepage.html')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = NewUserForm()
    return render(request=request,
                      template_name="dashboard/login.html",
                      context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request,"Logged Out!")
    return redirect("dashboard:homepage")

def homepage(request):
    return render(request=request,
                  template_name="dashboard/homepage.html")
