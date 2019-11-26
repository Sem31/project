from django import forms
from django.core.exceptions import ValidationError
from .models import Signup,Login
import base64


class CustomUserCreationForm(forms.Form):
    first_name = forms.CharField(label='Enter FirstName', min_length=4, max_length=30)
    username = forms.CharField(label='Enter Username', min_length=4, max_length=30)
    contact = forms.CharField(label='Enter Contact No', min_length=10, max_length=10)
    email = forms.EmailField(label='Enter email',max_length=50)
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput,)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput,)

    def clean_firstname(self):
        first_name = self.cleaned_data['first_name'].lower()
        r = Signup.objects.filter(first_name=first_name)
        if r.count():
            raise ValidationError("FirstName already exists")
        return first_name

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = Signup.objects.filter(user_name=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_contactno(self):
        contact = self.cleaned_data['contact'].lower()
        r = Signup.objects.filter(contact=contact)
        if r.count():
            raise ValidationError("Username already exists")
        return contact

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = Signup.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        password2 = base64.b64encode(password2.encode("utf-8"))

        return password2

    def save(self, commit=True):
        user = Signup.objects.create(
            first_name=self.cleaned_data['first_name'],
            user_name=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            contact = self.cleaned_data['contact'],
            password=self.cleaned_data['password2']
        )
        return user



class CustomUserLoginForm(forms.Form):
    email = forms.EmailField(label='Enter email',max_length=50)
    password = forms.CharField(label='Enter password', widget=forms.PasswordInput,)

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = Signup.objects.filter(email=email)

        if r.count():
            return email
        else :
            raise ValidationError("Email is not exists")


    def clean_password(self):
        password = self.cleaned_data.get('password')
        email = self.cleaned_data['email'].lower()
        r = Signup.objects.filter(email=email)
        password2 = base64.b64encode(password.encode("utf-8"))
        print(password2)
        if r.count():
            p = Signup.objects.values('password').filter(email=email)[0]
            print(p['password'])
            if str(p['password']) == str(password2):
                return password2
            else :
                raise ValidationError("Password is not exists")
        else :
            raise ValidationError("Password is not exists")


        return password2

    def save(self, commit=True):
        user = Login.objects.create(
            email=self.cleaned_data['email'],
            pasword=self.cleaned_data['password'],
        )
        return user