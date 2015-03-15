# -*- coding: utf-8 -*-
#!/usr/bin/env python
from project.accounts.forms import OrganizerProfileForm, UserRegistrationForm

from django.shortcuts import render, render_to_response
from project.accounts.profiles import retrieve
from project.accounts.models import OrganizerProfile, getOrganizerProfile, repopulateOrganizerProfile
from project.accounts.forms import OrganizerProfileForm, UserRegistrationForm, UserLoginForm
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from project.settings import ADMIN_EMAIL
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404


def profileView(request, template_name):
    user = request.user
    if user.is_authenticated():
        """проверка есть ли профиль у пользователя и получение его файл accounts.models"""
        profile = getOrganizerProfile(user)

    else:
        return HttpResponseRedirect(urlresolvers.reverse('registrationView'))
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

def populateProfileView(request, template_name):
    user = request.user
    form = OrganizerProfileForm()
    if user.is_authenticated():
        """проверка есть ли профиль у пользователя и получение его файл accounts.models"""
        profile = getOrganizerProfile(user)
        form = OrganizerProfileForm(instance=profile)
        if request.method == "POST":
            form = OrganizerProfileForm(request.POST, request.FILES)
            if form.is_valid() and getOrganizerProfile(user): #если профиль уже существует то только обновляем (не возвращает None)
                current_profile = getOrganizerProfile(user)
                current_profile = repopulateOrganizerProfile(current_profile, request)
                current_profile.save()
                return HttpResponseRedirect(urlresolvers.reverse('populateProfileView'))
            elif form.is_valid():
                form.save(request.user)
                return HttpResponseRedirect(urlresolvers.reverse('populateProfileView'))
            else: #должна быть обработка ошибок
                form = UserRegistrationForm(request.POST, request.FILES)
                return render(request, 'accounts/populate_profile.html', {
                    'form': form,
                    'error': form.errors,
                })
    else:
        return HttpResponseRedirect(urlresolvers.reverse('registrationView'))

    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

#регистрация пользователя
def registrationView(request, template_name):
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = UserRegistrationForm(postdata)
        terms = postdata.get('terms', '')
        if form.is_valid() and terms == 'on':

            form.save()
            un = postdata.get('username', '')
            # name="password1" т.к. два поля с подтверждением
            pw = postdata.get('password1', '')
            new_user = auth.authenticate(username=un, password=pw)
            if new_user and new_user.is_active:

                # отправляем e-mail о регистрации нового пользователя
                subject = u'sp.ru регистрация %s' % new_user.username
                message = u' Зарегистрирован новый пользователь %s / пароль: %s' % (new_user.username, pw)
                send_mail(subject, message, 'teamer777@gmail.com', [ADMIN_EMAIL], fail_silently=False)

                auth.login(request, new_user)
                # Редирект на url с именем my_account
                url = urlresolvers.reverse('profileView')
                return HttpResponseRedirect(url)
        elif terms == '':
            form = UserRegistrationForm(postdata)
            terms_error = 'пожалуйста подтвердите условия пользования сайтом'
            return render(request, 'accounts/registration.html', {
                'terms_error': terms_error,
                'form': form,
            })
        else:
            form = UserRegistrationForm(postdata)
            return render(request, 'accounts/registration.html', {
                'form': form,
                'error': form.errors,
            })
    else:
        form = UserRegistrationForm()
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

#страница входа для зарегистрированного пользователя
def loginView(request, template_name):
    form = UserLoginForm()
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = UserLoginForm(postdata)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
        # Правильный пароль и пользователь "активен"
            auth.login(request, user)
        # Перенаправление на "правильную" страницу
            return HttpResponseRedirect("/profile/")
        else:
            form = UserLoginForm(postdata)
            error = 'Логин или пароль введены не верно'
            return render(request, 'accounts/login.html', {
                'form': form,
                'error': error,
            })
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

def logoutView(request, template_name):
    user = request.user
    profile = getOrganizerProfile(user)
    if user.is_authenticated:
        auth.logout(request)
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
        # Правильный пароль и пользователь "активен"
            auth.login(request, user)
        # Перенаправление на "правильную" страницу
            return HttpResponseRedirect("/profile/")
        else:
            HttpResponseRedirect(urlresolvers.reverse('loginView'))
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

