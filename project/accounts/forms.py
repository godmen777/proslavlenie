# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django import forms
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils.translation import ugettext, ugettext_lazy as _
from project.accounts.models import OrganizerProfile, getOrganizerProfile
from django.forms import ModelForm, Form
from project.core.functions import *


class OrganizerProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrganizerProfileForm, self).__init__(*args, **kwargs)
        self.fields['firstName'].widget.attrs = {'placeholder':'Ваше Имя', 'class':'form-control'}
        self.fields['lastName'].widget.attrs = {'placeholder':'Ваша Фамилия', 'class':'form-control'}
        self.fields['email'].widget.attrs = {'placeholder':'Ваш e-mail', 'class':'form-control'}
        self.fields['phone'].widget.attrs = {'placeholder':'Ваш телефон', 'class':'form-control'}
        self.fields['address'].widget.attrs = {'placeholder':'Ваш адрес', 'class':'form-control'}
        self.fields['city'].widget.attrs = {'placeholder':'Ваш город', 'class':'form-control'}
        self.fields['zipCode'].widget.attrs = {'placeholder':'Почтовый индекс', 'class':'form-control'}
        self.fields['icon'].widget.attrs = {'class':'btn btn-block btn-default btn-sm'}

    class Meta:
        model = OrganizerProfile
        # widgets = {'user': forms.HiddenInput()}
        exclude = ('user',)

    def save(self, user):
        obj = super(OrganizerProfileForm, self).save(commit=False)
        obj.user = user
        return obj.save()

class UserRegistrationForm(forms.ModelForm):
    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }
    username = forms.RegexField(label=_("Username"), max_length=100,
        regex=r'^[\w.@+-]+$',
        error_messages = {'invalid': "Это значение может состоять из латинских букв, цифр и знаков @/./+/-/_."},
        widget=forms.TextInput(attrs={'placeholder': 'Ваше Имя', 'class': 'form-control'}),
    )
    email = forms.EmailField(
        label=_("Email"),
        error_messages = {'invalid': "Введите корректный e-mail адрес"},
        widget=forms.TextInput(attrs={'placeholder': 'Ваш e-mail', 'class': 'form-control'}),
    )
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ("username",)

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserLoginForm(forms.ModelForm):
    error_messages = {
        'wrong': ("Имя пользователя или пароль введены неверно"),
    }
    username = forms.RegexField(label=_("Username"), max_length=100,
        regex=r'^[\w.@+-]+$',
        error_messages = {'invalid': "Это значение может состоять из латинских букв, цифр и знаков @/./+/-/_."},
        widget=forms.TextInput(attrs={'placeholder': 'Ваше Имя', 'class': 'form-control'}),
    )
    password = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = ("username",)










