# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.db import models
from django.db.models import permalink
from autoslug import AutoSlugField
from mptt.models import MPTTModel, TreeForeignKey


class MenuCategory(MPTTModel):
    name = models.CharField(u'Название категории', max_length=50, unique=True)
    slug = models.SlugField(u'Ссылка', max_length=50, unique=True,)
    parent = TreeForeignKey('self', verbose_name=u'Родительская категория',
                            related_name='children', blank=True,
                            help_text=u'Родительская категория для этой категории', null=True)
    created_at = models.DateTimeField(u'Дата создания', auto_now_add=True)
    class Meta:
        verbose_name = u'Раздел меню служения'
        verbose_name_plural = u'Меню служения'
    def __unicode__(self):
        # return self.name
        return '%s%s' % ('--' * self.level, self.name)
    def url(self):
        return '/ministry/%s' % self.slug


# class MenuItem(models.Model):
#     menu_category = models.ForeignKey(MenuCategory)
#     name = models.CharField(max_length=200, verbose_name=u'Название ссылки меню')
#     slug = models.SlugField(u'Ссылка', max_length=50, unique=True)
#
#     def url(self):
#         return '/ministry/%s/%s' % (self.menu_category.slug, self.slug)