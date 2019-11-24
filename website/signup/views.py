from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'pakhi-web/index.html')


def user_registration(request):
    form = CustomUserCreationForm(request.POST or None, request.FILES or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registerd')
            return redirect('/')
        # If the request params is valid save the data else return form with error
    return render(request, 'registration/registration.html', {'form': form})

@login_required(login_url='/accounts/login')
def user_profile(request):
    return render(request, 'pakhi-web/user_profile.html', {'user': request.user})



    

