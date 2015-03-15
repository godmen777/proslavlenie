# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django import template
from project.accounts.models import getOrganizerProfile
from project.menu.models import MenuCategory


register = template.Library()

# The first argument *must* be called "context" here.
def coreLeftMenu(context, request):
    user = request.user
    if user.is_authenticated():
        profile = getOrganizerProfile(user)
        return {
            'user': user,
            'profile': profile,
        }
    else:
        return {
            'user': user,
        }
# Register the custom tag as an inclusion tag with takes_context=True.
register.inclusion_tag('core/tags/core_left_menu.html', takes_context=True)(coreLeftMenu)

def coreTopMenu(context, request):
    user = request.user
    if user.is_authenticated():
        profile = getOrganizerProfile(user)
        return {
            'user': user,
            'profile': profile,
        }
    else:
        return {
            'user': user,
        }

# Register the custom tag as an inclusion tag with takes_context=True.
register.inclusion_tag('core/tags/core_top_menu.html', takes_context=True)(coreTopMenu)

def menu_tree(context, request):
    return {
        'menu_objects': MenuCategory.objects.all(),

    }
register.inclusion_tag('core/tags/menu_category.html', takes_context=True)(menu_tree)