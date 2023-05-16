from django import forms
from django.core.exceptions import ValidationError

from django.contrib.auth.forms import UserCreationForm

from account.validators import length_validator


class RegisterForm(forms.Form):
    Email = forms.EmailField()
    Password = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=32)
    Password_Confirmation = forms.CharField(widget=forms.PasswordInput)

    def clean_Password_Confirmation(self):
        password_confirmation = self.cleaned_data['Password_Confirmation']
        password = self.cleaned_data['Password']
        if password_confirmation != password:
            raise ValidationError('password does not match to confirmation password!')
        return password_confirmation


class LoginForm(forms.Form):
    Email = forms.EmailField()
    Password = forms.CharField(widget=forms.PasswordInput)
