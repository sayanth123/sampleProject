from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=60)
    last_name=forms.CharField(max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField(label='Enter password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput)

    class Meta:
	    model = User
	    fields = ("first_name","last_name","username", "email", "password1", "password2")

    help_text = {
        "username": None,
    }
