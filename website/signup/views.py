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
        print("hi kamlesh")
        if form.is_valid():
            print("buy kamlesh")
            form.save()
            messages.success(request, 'Successfully registerd')
            return redirect('/')
        # If the request params is valid save the data else return form with error
    return render(request, 'pakhi-web/signin.html', {'form': form})

def user_profile(request):
    return render(request, 'pakhi-web/signin.html', {'user': request.user})

