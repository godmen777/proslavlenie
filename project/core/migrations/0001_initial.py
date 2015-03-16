# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SliderItem'
        db.create_table(u'core_slideritem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'core', ['SliderItem'])

        # Adding model 'Article'
        db.create_table(u'core_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('description', self.gf('ckeditor.fields.RichTextField')()),
            ('sub_title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('entry', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('cropping', self.gf(u'django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
            ('slider', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.SliderItem'], unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Article'])

        # Adding model 'News'
        db.create_table(u'core_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('ckeditor.fields.RichTextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('cropping', self.gf(u'django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
        ))
        db.send_create_signal(u'core', ['News'])

        # Adding model 'Page'
        db.create_table(u'core_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('description', self.gf('ckeditor.fields.RichTextField')()),
            ('slider', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.SliderItem'], unique=True)),
        ))
        db.send_create_signal(u'core', ['Page'])

        # Adding model 'ArticleGalleryImage'
        db.create_table(u'core_articlegalleryimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Article'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('cropping', self.gf(u'django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
        ))
        db.send_create_signal(u'core', ['ArticleGalleryImage'])

        # Adding model 'NewsGalleryImage'
        db.create_table(u'core_newsgalleryimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('news', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.News'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('cropping', self.gf(u'django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
        ))
        db.send_create_signal(u'core', ['NewsGalleryImage'])

        # Adding model 'PageGalleryImage'
        db.create_table(u'core_pagegalleryimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Page'])),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'core', ['PageGalleryImage'])


    def backwards(self, orm):
        # Deleting model 'SliderItem'
        db.delete_table(u'core_slideritem')

        # Deleting model 'Article'
        db.delete_table(u'core_article')

        # Deleting model 'News'
        db.delete_table(u'core_news')

        # Deleting model 'Page'
        db.delete_table(u'core_page')

        # Deleting model 'ArticleGalleryImage'
        db.delete_table(u'core_articlegalleryimage')

        # Deleting model 'NewsGalleryImage'
        db.delete_table(u'core_newsgalleryimage')

        # Deleting model 'PageGalleryImage'
        db.delete_table(u'core_pagegalleryimage')


    models = {
        u'core.article': {
            'Meta': {'object_name': 'Article'},
            'cropping': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'description': ('ckeditor.fields.RichTextField', [], {}),
            'entry': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slider': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.SliderItem']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'sub_title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'core.articlegalleryimage': {
            'Meta': {'object_name': 'ArticleGalleryImage'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Article']"}),
            'cropping': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'core.news': {
            'Meta': {'object_name': 'News'},
            'cropping': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'description': ('ckeditor.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'core.newsgalleryimage': {
            'Meta': {'object_name': 'NewsGalleryImage'},
            'cropping': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'news': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.News']"})
        },
        u'core.page': {
            'Meta': {'object_name': 'Page'},
            'description': ('ckeditor.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slider': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.SliderItem']", 'unique': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'core.pagegalleryimage': {
            'Meta': {'object_name': 'PageGalleryImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Page']"})
        },
        u'core.slideritem': {
            'Meta': {'object_name': 'SliderItem'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['core']