# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.contrib import admin
from mptt_tree_editor.admin import TreeEditor
from project.menu.models import MenuCategory

# Register your models here.
class MenuCategoryAdmin(TreeEditor):
    """
    Управление категориями
    Как будут отображаться поля категорий в разделе администрирования
    """
    list_display = ("indented_short_title", "actions_column", 'name')
    list_display_links = ('name',)
    # list_per_page = 20
    ordering = ['created_at']
    search_fields = ['name']
    readonly_fields = ('created_at',)
    # exclude = ('created_at', 'updated_at',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(MenuCategory, MenuCategoryAdmin)