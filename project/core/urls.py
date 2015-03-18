# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.conf.urls import patterns, url

urlpatterns = patterns('project.core.views',


    # Главная страница
    url(r'^$', 'indexView',
        {'template_name':'core/index.html'},
        name='indexView'),

    url(r'^articles/(?P<slug>[-\w]+)/$', 'articleView',
        {'template_name':'core/article.html'},
        name='articleView'),

    url(r'^news/$', 'newsAllView',
        {'template_name':'core/news_all.html'},
        name='newsAllView'),
    url(r'^news/(?P<id>[-\w]+)/$', 'newsView',
        {'template_name':'core/news.html'},
        name='newsView'),

    url(r'^reviews/$', 'reviewsView',
        {'template_name':'core/reviews.html'},
        name='reviewsView'),
    url(r'^review/(?P<id>[-\w]+)/$', 'reviewView',
        {'template_name':'core/review.html'},
        name='reviewView'),

    url(r'^testimonys/$', 'testimonysView',
        {'template_name':'core/testimonys.html'},
        name='testimonysView'),
    url(r'^testimony/(?P<id>[-\w]+)/$', 'testimonyView',
        {'template_name':'core/testimony.html'},
        name='testimonyView'),

)
