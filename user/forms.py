from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student


class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Student
        fields = ['username', 'email', 'password1', 'password2']


class StudentLoginForm(forms.Form):
    username = forms.CharField(max_length=191)
    password = forms.CharField(widget=forms.PasswordInput)
