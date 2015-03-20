# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.shortcuts import render
from django.template import RequestContext
from django.core import urlresolvers
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.core.context_processors import csrf
from project.core.functions import *
from project.accounts.models import getOrganizerProfile
from project.accounts.forms import OrganizerProfileForm, UserRegistrationForm
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from project.core.models import Article, ArticleGalleryImage, Page, PageGalleryImage, News, SliderItem, Review, Testimony, Video
from project.menu.models import MenuCategory


def indexView(request, template_name="catalog/index.html"):
    user = request.user
    articles = Article.objects.all()
    news = News.objects.all()[:5]
    menu_objects = MenuCategory.objects.all()
    slides = SliderItem.objects.all()[:3]
    # получение ссылок для видео
    try:        
        main_video = Video.objects.filter(category=1).last()
        main_video.video = main_video.video[17:]
    except:
        None
    try:
        pritch_video = Video.objects.filter(category=2).last()
        pritch_video.video = pritch_video.video[17:]
    except:
        None
    # for slide in slides:
    #     try:
    #         slide.article = Article.objects.get(slider=slide.id)
    #     except:
    #         None
    reviews = Review.objects.all()[:2]


    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


def articleView(request, slug, template_name="catalog/article.html"):
    user = request.user
    article = Article.objects.get(slug=slug)

    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


def newsView(request, id, template_name="catalog/news.html"):
    user = request.user
    news = News.objects.get(id=id)

    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

def newsAllView(request, template_name="catalog/news_all.html"):
    news_all = News.objects.all()
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

def reviewsView(request, template_name="catalog/reviews.html"):
    reviews = Review.objects.all()
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

def reviewView(request, id, template_name="catalog/review.html"):
    review = Review.objects.get(id=id)
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

def testimonysView(request, template_name="catalog/reviews.html"):
    testimonys = Testimony.objects.all()
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

def testimonyView(request, id, template_name="catalog/testimony.html"):
    user = request.user
    testimony = Testimony.objects.get(id=id)

    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))