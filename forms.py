from django import forms
from .models import Account
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


class AccountForm(UserCreationForm):
    email = forms.EmailField(max_length=30, help_text="Required Email Address")
    number = forms.CharField(max_length=17, help_text="Required Phone Number")

    class Meta:
        model = Account
        fields = ['username', 'email', 'number', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} is already in use")

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        try:
            account = Account.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"Username {username} is already in use")


class AccountLoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ['email', 'password']

    def clean(self):
        email = self.cleaned_data.get('email').lower()
        password = self.cleaned_data.get('password')
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Invalid Login')
