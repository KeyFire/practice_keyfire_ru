# coding: utf-8
from django import forms
from django.contrib.auth.models import User
from userprofile.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['website', 'username']


class UserForm(forms.ModelForm):
    model = User
    fields = ['username']