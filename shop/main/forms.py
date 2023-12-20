from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import User_Custom


class FuncLogin(AuthenticationForm):


    username=forms.CharField(widget=forms.TextInput(attrs=
                        {
                            'Placeholder':' Input Username',
                            'class':'w-full py-4 px-6 rounded-xl',

                        }))

    password=forms.CharField(widget=forms.PasswordInput(attrs=
                        {
                            'Placeholder':' Input password',
                            'class':'w-full py-4 px-6 rounded-xl',

                        }))



class FuncSignup(UserCreationForm):
    class Meta:
        model= User_Custom
        fields=('email','username','password1','password2')

    username=forms.CharField(widget=forms.TextInput(attrs=
                        {
                            'Placeholder':' Input Username',
                            'class':'w-full py-4 px-6 rounded-xl',

                        }))
    email=forms.CharField(widget=forms.EmailInput(attrs=
                        {
                            'Placeholder':' Input email',
                            'class':'w-full py-4 px-6 rounded-xl',

                        }))
    
    password1=forms.CharField(widget=forms.PasswordInput(attrs=
                        {
                            'Placeholder':' Input password',
                            'class':'w-full py-4 px-6 rounded-xl',

                        }))
    
    password2=forms.CharField(widget=forms.PasswordInput(attrs=
                        {
                            'Placeholder':' Repeat Password',
                            'class':'w-full py-4 px-6 rounded-xl',

                        }))