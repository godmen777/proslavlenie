# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Video.cropping'
        db.add_column(u'core_video', 'cropping',
                      self.gf(u'django.db.models.fields.CharField')(default=u'', max_length=255, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Video.cropping'
        db.delete_column(u'core_video', 'cropping')


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
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
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
        u'core.review': {
            'Meta': {'object_name': 'Review'},
            'cropping': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'input_video': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'core.slideritem': {
            'Meta': {'object_name': 'SliderItem'},
            'cropping': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'core.testimony': {
            'Meta': {'object_name': 'Testimony'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'core.testimonygalleryimage': {
            'Meta': {'object_name': 'TestimonyGalleryImage'},
            'cropping': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'testimony': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Testimony']"})
        },
        u'core.video': {
            'Meta': {'object_name': 'Video'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.VideoCategory']", 'blank': 'True'}),
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'cropping': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'video': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'core.videocategory': {
            'Meta': {'object_name': 'VideoCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['core']