from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.http import request
# from .wallet_generator import wallet_address


# Create forms
class SapanoUserCreateUser(UserCreationForm):
    username = forms.CharField(label='Username', max_length=25,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Username',
                                   'class': 'form-control'
                               }))

    email = forms.EmailField(label='Email Address', required=True,
                             widget=forms.EmailInput(attrs={
                                 'placeholder': 'yourname@email.com',
                                 'class': 'form-control'
                             }))

    country = forms.CharField(label='Country', max_length=25,
                              widget=forms.TextInput(attrs={
                                  'placeholder': 'Choose your country',
                                  'class': 'form-control'
                              }))

    phone = forms.CharField(label='Phone Number', max_length=25,
                            widget=forms.TextInput(attrs={
                                'placeholder': 'Telephone Number',
                                'class': 'form-control',
                                'type': 'telephone'
                            }))

    Dob = forms.DateInput()

    password1 = forms.Field(label='Password', required=True,
                            widget=forms.PasswordInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Password'
                            }))

    password2 = forms.Field(label='Confirm password', required=True,
                                widget=forms.PasswordInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Confirm Password'
                            }))

    required_css_class = "bootstrap5-req"

    def username_clean(self):
        self.username = self.cleaned_data['username'].lower()
        new = User.objects.filter(usernmae=self.username)

        if new.count():
            print('wahala name')
        return self.username

    def email_clean(self):
        self.email = self.cleaned_data['email'].lower()
        new = User.objects.filter(eamil=self.email)

        if new.count():
            print('wahala email')

        return self.email

    def clean_password2(self):
        self.password1 = self.cleaned_data['password1']
        self.password2 = self.cleaned_data['password2']

        if self.password1 and self.password2 and self.password1 != self.password2:
            print('wahala, unmatch password')
        return self.password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class SapanoUserLogin(AuthenticationForm):
    username = forms.CharField(max_length=25, widget=forms.TextInput(attrs={
                                   'placeholder': 'Username',
                                   'class': 'form-control',
                                   'placeholder': 'Username'
                               }))

    password = forms.CharField(max_length=25, widget=forms.PasswordInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Password'
                            }))
    