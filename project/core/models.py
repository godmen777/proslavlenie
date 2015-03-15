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


class BaseArticle(models.Model):
    class Meta:
        abstract = True
    name = models.CharField(max_length=200, verbose_name=u'Название материала')
    slug = models.SlugField(u'Ссылка', max_length=50, unique=True)
    description = RichTextField()


# единица слайдера , связи 1 к 1 со статьями и со страницами
class SliderItem(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Название слайдера')
    description = models.TextField(verbose_name=u'Описание слайдера')
    image = models.FileField(verbose_name=u'Изображение для слайдера', upload_to='slider', blank=True)
    def __unicode__(self):
        return _(u'Слайдер: ') + self.name



class Article(BaseArticle):
    sub_title = models.CharField(max_length=60, verbose_name=u'Подзаголовок')
    entry = models.TextField(verbose_name=u'Вступление')
    image = models.ImageField(verbose_name=u'Банер', upload_to='articles/images/', blank=True)
    cropping = ImageRatioField('image', '340x340', verbose_name=u'Иконка')
    slider = models.OneToOneField(SliderItem, blank=True, null=True)
    def __unicode__(self):
        return _(u'Статья: ') + self.name
    def get_gallery_images(self):
        return  ArticleGalleryImage.objects.filter(article=self.id)
    def image_url(self):
        return '/media/%s' % self.image
    def url(self):
        return '/articles/%s' % self.slug


class News(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Название новости')
    description = RichTextField()
    image = models.ImageField(verbose_name=u'Изображение', upload_to='news/images/', blank=True)
    cropping = ImageRatioField('image', '340x340', verbose_name=u'Иконка')
    date = models.DateField(verbose_name=u'Дата', default=datetime.datetime.now, editable=True)
    def __unicode__(self):
        return _(u'Новость: ') + self.name
    def get_gallery_images(self):
        return  NewsGalleryImage.objects.filter(news=self.id)
    def image_url(self):
        return '/media/%s' % self.image
    def url(self):
        return '/news/%s' % self.id



class Page(BaseArticle):
    slider = models.OneToOneField(SliderItem)
    def __unicode__(self):
        return _(u'Страница: ') + self.name



class ArticleGalleryImage(models.Model):
    article = models.ForeignKey(Article)
    image = models.ImageField(verbose_name=u'Изображение для галереи', upload_to='gallery_article', blank=True)
    cropping = ImageRatioField('image', '340x340')
    def url(self):
        return "/media/%s" % self.image


class NewsGalleryImage(models.Model):
    news = models.ForeignKey(News)
    image = models.ImageField(verbose_name=u'Изображение для галереи', upload_to='gallery_news', blank=True)
    cropping = ImageRatioField('image', '340x340')
    def url(self):
        return "/media/%s" % self.image



class PageGalleryImage(models.Model):
    page = models.ForeignKey(Page)
    image = models.FileField(verbose_name=u'Изображение для галереи', upload_to='gallery_page', blank=True)
