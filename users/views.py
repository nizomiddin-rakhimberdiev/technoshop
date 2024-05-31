from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from products.models import Product
from products.views import home_page
from users.forms import RegisterForm


# Create your views here.
def login_page(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('products:index')
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})


def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {"form": form})


def logout_page(request):
    logout(request)
    return redirect('products:index')



