# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.contrib import admin
from project.core.models import Article, Page, SliderItem, ArticleGalleryImage, NewsGalleryImage, PageGalleryImage, News
from image_cropping import ImageCroppingMixin
from cicu.widgets import CicuUploderInput
from django import forms


class ArticleImagesInline(ImageCroppingMixin, admin.StackedInline):
    """Вывод заказов списком"""
    model = ArticleGalleryImage
    extra = 0

class NewsImagesInline(ArticleImagesInline):
    model = NewsGalleryImage

class PageImagesInline(admin.StackedInline):
    model = PageGalleryImage
    extra = 0

class ArticleAdmin(ImageCroppingMixin, admin.ModelAdmin):
    model = Article
    fields = (('name', 'slug'), 'sub_title','entry', 'description', 'image', 'cropping', 'slider')
    inlines = [ArticleImagesInline]
    prepopulated_fields = {'slug':('name',),}

class NewsAdmin(ImageCroppingMixin, admin.ModelAdmin):
    model = News
    inlines = [NewsImagesInline]
    fields = ('name', 'date', 'description', 'image', 'cropping' )

class PageAdmin(admin.ModelAdmin):
    model = Page
    inlines = [PageImagesInline]
    # prepopulated_fields = {'slug':('id',)}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(SliderItem)
admin.site.register(News, NewsAdmin)
