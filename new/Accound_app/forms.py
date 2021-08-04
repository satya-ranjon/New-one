from django import forms 
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import fields 


class Login_user(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': ' Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': ' Password',
        'id':'myinput1',
    }))
    class Meta:
        model = User
        fields = ('username','password',)


class sign_user(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': ' Username'
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': ' example..@gmail.com'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': ' Password',
        'id':'myinput1',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': ' Confirm Password',
        'id':'myinput2',
    }))
    class Meta:
        model = User
        fields = ('username','email','password1','password2')


class Change_password(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':' Old Password input',
        'id':'myinput1',
    }))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':' New Password',
        'id':'myinput2',
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':' Confirm Password',
        'id':'myinput3',
    }))
    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')






