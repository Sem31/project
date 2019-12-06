from django.shortcuts import render,redirect
from .forms import UserSignupForm,UserLoginForm
from .models import Signup

# Create your views here.


def index(request):
	if 'username' in request.session:
		username = request.session['username']
		return render(request,'profile.html',{'username':username})
	return render(request,'index.html')


def userSignup(request):
	username = "not logged in"
	if request.method == 'POST':
		form = UserSignupForm(request.POST or None)
		if form.is_valid():
			form.save()
			name = form.cleaned_data['name']
			request.session['username'] = name
			return redirect('home')
	else :
		form = UserSignupForm()
	return render(request,'signin.html',{'form':form})



def userLogin(request):
	if request.method == 'POST':
		form = UserLoginForm(request.POST or None)
		mobile = request.POST.get('mobile')
		password1 = request.POST.get('password1')
		if form.is_valid():
			user = Signup.objects.filter(mobile=mobile)[0]
			print(user.password)
			if password1 == user.password:
				request.session['username'] = user.name
				return redirect('home')
	else :
		form = UserLoginForm()
	return render(request,'signin.html',{'form':form})



def userLogout(request):
	del request.session['username']
	return redirect('home')


# def userProfile(request):
# 	if 'username' in request.session:
# 		username = request.session['username']
# 		return render(request,'profile.html',{'username':username})
# 	return redirect('home')