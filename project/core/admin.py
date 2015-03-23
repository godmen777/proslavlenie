# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.contrib import admin
from project.core.models import Article, Page, SliderItem, ArticleGalleryImage, NewsGalleryImage, PageGalleryImage
from project.core.models import News, Review, Testimony, TestimonyGalleryImage, Video, VideoCategory
from image_cropping import ImageCroppingMixin
from django import forms


class ArticleImagesInline(ImageCroppingMixin, admin.StackedInline):
    """Вывод заказов списком"""
    model = ArticleGalleryImage
    extra = 0

class NewsImagesInline(ArticleImagesInline):
    model = NewsGalleryImage

class TestimonyImagesInline(ArticleImagesInline):
    model = TestimonyGalleryImage

class PageImagesInline(admin.StackedInline):
    model = PageGalleryImage
    extra = 0

class VideoCategoryInline(admin.StackedInline):
    """Вывод заказов списком"""
    model = VideoCategory
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

class TestimonyAdmin(ImageCroppingMixin, admin.ModelAdmin):
    model = News
    inlines = [TestimonyImagesInline]
    fields = ('name', 'description', 'image' )

class PageAdmin(admin.ModelAdmin):
    model = Page
    inlines = [PageImagesInline]

class SliderItemAdmin(ImageCroppingMixin, admin.ModelAdmin):
    model = SliderItem

class VideoAdmin(ImageCroppingMixin, admin.ModelAdmin):
    model = Video
    fields = ('name', 'description', 'video', 'category', 'cover', ('cropping', 'cropping_pritch', 'cropping_videoblog'))

# class VideoAdmin(admin.ModelAdmin):
#     model = Video
#     inlines = [VideoCategoryInline]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(SliderItem, SliderItemAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Review)
admin.site.register(Testimony, TestimonyAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(VideoCategory)