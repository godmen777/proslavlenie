# -*- coding: utf-8 -*-
#!/usr/bin/env python

from django.contrib import admin
from django.contrib.auth.models import User
from project.accounts.models import BaseUserInfo, OrganizerProfile
from project.core.models import Article, Page, SliderItem
# Register your models here.

admin.site.register(OrganizerProfile)



