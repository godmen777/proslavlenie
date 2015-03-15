# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.contrib import admin
from project.core.models import Article, Page, SliderItem, ArticleGalleryImage, PageGalleryImage
from image_cropping import ImageCroppingMixin
from cicu.widgets import CicuUploderInput
from django import forms


class ArticleImagesInline(ImageCroppingMixin, admin.StackedInline):
    """Вывод заказов списком"""
    model = ArticleGalleryImage
    extra = 0

class PageImagesInline(admin.StackedInline):
    """Вывод заказов списком"""
    model = PageGalleryImage
    extra = 0

class ArticleAdmin(ImageCroppingMixin, admin.ModelAdmin):
    model = Article
    fields = (('name', 'slug'), 'sub_title','entry', 'description', 'image', 'cropping', 'slider')
    inlines = [ArticleImagesInline]
    prepopulated_fields = {'slug':('name',),}

class PageAdmin(admin.ModelAdmin):
    model = Page
    inlines = [PageImagesInline]
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(SliderItem)
