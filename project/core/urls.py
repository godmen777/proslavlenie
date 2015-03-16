# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.conf.urls import patterns, url

urlpatterns = patterns('project.core.views',

    # url(r'^viewproduct/$', 'viewProduct',
		# {'template_name':'core/viewproduct.html'},
		# name='viewproduct'),
    #
    #
    #
    # # Главная страница
    url(r'^$', 'indexView',
		{'template_name':'core/index.html'},
		name='indexView'),
    url(r'^articles/(?P<slug>[-\w]+)/$', 'articleView',
		{'template_name':'core/article.html'},
		name='articleView'),
    url(r'^news/(?P<id>[-\w]+)/$', 'newsView',
		{'template_name':'core/news.html'},
		name='newsView'),
    url(r'^reviews/$', 'reviewsView',
		{'template_name':'core/reviews.html'},
		name='reviewsView'),
    # url(r'^purchase-(\d+)/$', 'corePurchase',
		# {'template_name': 'core/core_purchase.html'},
		# name='corePurchase'),
    # url(r'^purchase-(?P<purchase_id>\d+)/catalog-(?P<catalog_id>\d+)/$', 'coreCatalog',
		# {'template_name': 'core/core_catalog.html'},
		# name='coreCatalog'),



    # Страницы сайта
    # url(r'^(?P<slug>[-\w]+)/$', 'page_view',
    #     {'template_name':'main/page.html'},
    #     name='page_view'),
)
