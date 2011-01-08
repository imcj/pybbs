#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

from django.contrib import admin
from pybbs.models import Topic, Reply

class ReplyInLine ( admin.TabularInline ):
    model = Reply
    
class TopicAdmin ( admin.ModelAdmin ):
    inlines = [ ReplyInLine ]

admin.site.register ( Topic, TopicAdmin )