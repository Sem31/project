from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm,CustomUserLoginForm
from django.contrib import messages
from .models import Signup

# Create your views here.


def user_registration(request):
    form = CustomUserCreationForm()

    print(form)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            context = form.save()
            return redirect(user_welcome,context)
    return render(request, 'pakhi-web/registration/registration.html', {'form': form})


def user_login(request):
    form = CustomUserLoginForm()

    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            context = form.save()
            return redirect(user_welcome,context)
    return render(request,'pakhi-web/registration/login.html',{'form':form})


def user_welcome(request,context):
    return render(request, 'pakhi-web/after_signup.html')




