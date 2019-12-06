from django import forms
from .models import Signup



class UserSignupForm(forms.Form):
	name = forms.CharField(min_length=4,max_length=20)
	mobile = forms.CharField(min_length=10,max_length=10)
	email = forms.EmailField(max_length=40)
	password1 = forms.CharField(min_length=8,max_length=20,widget=forms.PasswordInput)
	password2 = forms.CharField(min_length=8,max_length=20,widget=forms.PasswordInput)

	# def clean_password1(self):
	# 	password1 = self.cleaned_data['password1']
	# 	password2 = self.cleaned_data['password2']

	# 	if password1 and password2 and password1 != password2:
	# 		raise ValidationError("Password don't match")

	# 	p = base64.b64encode(password1.encode("utf-8"))	
	# 	password1 = str(p, "utf-8")
	# 	return password1

	def save(self):
		user = Signup.objects.create(
			name = self.cleaned_data['name'],
			mobile = self.cleaned_data['mobile'],
			email = self.cleaned_data['email'],
			password =self.cleaned_data['password1']
			)


class UserLoginForm(forms.Form):
	mobile = forms.CharField(min_length=10,max_length=10)
	password1 = forms.CharField(min_length=8,max_length=20,widget=forms.PasswordInput)