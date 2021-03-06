# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.db import models
import datetime
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from project.core.functions import *
from autoslug import AutoSlugField
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from image_cropping import ImageRatioField

"""Базовый класс"""
class BaseArticle(models.Model):
    class Meta:
        abstract = True
    name = models.CharField(max_length=200, verbose_name=u'Название материала')
    slug = models.SlugField(u'Ссылка', max_length=50, unique=True)
    description = RichTextField()


"""Блок слайдера"""
# единица слайдера , связи 1 к 1 со статьями и со страницами
class SliderItem(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Название слайдера')
    link = models.CharField(max_length=200, verbose_name=u'Ссылка на материал', help_text=u'Ссылка должна быть относительной и начинаться с корня сайта со знака "/" \n пример ссылки "/news/1" ')
    date = models.DateField(verbose_name=u'Дата', default=datetime.datetime.now, editable=True)
    description = models.TextField(verbose_name=u'Описание слайдера')
    image = models.ImageField(verbose_name=u'Изображение для слайдера', upload_to='slider', blank=True)
    cropping = ImageRatioField('image', '880x320', verbose_name=u'Обрезка фото')
    class Meta:
        verbose_name = u'Слайд'
        verbose_name_plural = u'Слайдер на главной'
    def __unicode__(self):
        return _(u'Слайдер: ') + self.name
    def url(self):
        return '/media/%s' % self.image


"""Блок Статьи"""
class Article(BaseArticle):
    sub_title = models.CharField(max_length=60, verbose_name=u'Подзаголовок')
    entry = models.TextField(verbose_name=u'Вступление')
    image = models.ImageField(verbose_name=u'Банер', upload_to='articles/images/', blank=True)
    cropping = ImageRatioField('image', '340x340', verbose_name=u'Иконка')
    slider = models.OneToOneField(SliderItem, blank=True, null=True)
    class Meta:
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'
    def __unicode__(self):
        return _(u'Статья: ') + self.name
    def get_gallery_images(self):
        return  ArticleGalleryImage.objects.filter(article=self.id)
    def image_url(self):
        return '/media/%s' % self.image
    def url(self):
        return '/articles/%s' % self.slug

class ArticleGalleryImage(models.Model):
    article = models.ForeignKey(Article)
    image = models.ImageField(verbose_name=u'Изображение для галереи', upload_to='gallery_article', blank=True)
    cropping = ImageRatioField('image', '340x340')
    def url(self):
        return "/media/%s" % self.image


"""Блок новости"""
class News(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Название новости')
    description = RichTextField()
    image = models.ImageField(verbose_name=u'Изображение', upload_to='news/images/', blank=True)
    cropping = ImageRatioField('image', '275x200', verbose_name=u'Иконка')
    date = models.DateField(verbose_name=u'Дата', default=datetime.datetime.now, editable=True)
    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'
    def __unicode__(self):
        return _(u'Новость: ') + self.name
    def get_gallery_images(self):
        return  NewsGalleryImage.objects.filter(news=self.id)
    def image_url(self):
        return '/media/%s' % self.image
    def url(self):
        return '/news/%s' % self.id

class NewsGalleryImage(models.Model):
    news = models.ForeignKey(News)
    image = models.ImageField(verbose_name=u'Изображение для галереи', upload_to='gallery_news', blank=True)
    cropping = ImageRatioField('image', '175x120')
    def url(self):
        return "/media/%s" % self.image


"""Блок Отзывы"""
class Review(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Имя')
    description = models.TextField(verbose_name=u'Отзыв')
    input_video = models.CharField(max_length=240, verbose_name=u'поле для вставки видео из youtube')
    date = models.DateField(verbose_name=u'Дата', default=datetime.datetime.now, editable=True)
    image = models.ImageField(verbose_name=u'Изображение', upload_to='reviews', blank=True)
    cropping = ImageRatioField('image', '275x200', verbose_name=u'Иконка')
    class Meta:
        verbose_name = u'Отзыв'
        verbose_name_plural = u'Отзывы'
    def __unicode__(self):
        return _(u'Отзыв: ') + self.name
    def url(self):
        return u"/review/%s" % self.id


"""Блок Свидетельства"""
class Testimony(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Ваше имя')
    description = models.TextField(verbose_name=u'Ваше свидетельство')
    image = models.ImageField(verbose_name=u'Фото для свидетельства', upload_to='gallery_testimony', blank=True)
    class Meta:
        verbose_name = u'Свидетельство'
        verbose_name_plural = u'Свидетельства'
    def __unicode__(self):
        return u'Свидетельство %s' % self.name
    def url(self):
        return u'/testimony/%s' % self.id
    def get_gallery_images(self):
        return  TestimonyGalleryImage.objects.filter(testimony=self.id)

class TestimonyGalleryImage(models.Model):
    testimony = models.ForeignKey(Testimony)
    image = models.ImageField(verbose_name=u'Изображение для галереи', upload_to='gallery_testimony', blank=True)
    cropping = ImageRatioField('image', '175x120')
    def url(self):
        return "/media/%s" % self.image


"""Блок Свидетельства"""
class VideoCategory(models.Model):
    name = models.CharField(verbose_name=u'Название видео категории', max_length=200)
    def __unicode__(self):
        return u'Видео категория: %s' % self.name

class Video(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Название')
    description = models.TextField(verbose_name=u'Описание')
    cover = models.ImageField(verbose_name=u'Обложка', upload_to='covers', blank=True)
    cropping = ImageRatioField('cover', '479x320', verbose_name=u'Обложка основного видео на главной')
    cropping_pritch = ImageRatioField('cover', '173x150', verbose_name=u'Обложка проповеди на главной')
    cropping_videoblog = ImageRatioField('cover', '275x200', verbose_name=u'Обложка видеоблог на главной')
    video = models.CharField(verbose_name=u'ссылка на видео youtube', max_length=200, help_text=u'вводите ссылку на видео которая получается в результате нажатия на кнопку поделиться в youtube, например "https://youtu.be/t42-71RpRgI?t=1h41m40s" ')
    category = models.ForeignKey(VideoCategory, verbose_name=u'Выбрать категорию для видео', blank=True)
    class Meta:
        verbose_name = u'Видео материал'
        verbose_name_plural = u'Видео контент'
    def __unicode__(self):
        return u'Видео %s' % self.name


class Page(BaseArticle):
    slider = models.OneToOneField(SliderItem)
    def __unicode__(self):
        return _(u'Страница: ') + self.name

class PageGalleryImage(models.Model):
    page = models.ForeignKey(Page)
    image = models.FileField(verbose_name=u'Изображение для галереи', upload_to='gallery_page', blank=True)
