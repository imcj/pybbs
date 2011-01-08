#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

from django import forms
from pybbs.models import Topic, Reply

class TopicForm ( forms.ModelForm ):
    class Meta:
        model = Topic
        fields = ( 'subject', 'body', )