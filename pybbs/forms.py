#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

from django import forms
from django.shortcuts import get_object_or_404
from pybbs.models import Topic, Reply, Category

class TopicForm ( forms.ModelForm ):
    class Meta:
        model = Topic
        fields = ( 'subject', 'slug', 'body', )
    
    def __init__ ( self, user = None, *args, **kwargs ):
        self.user = user
        super ( TopicForm, self ).__init__ ( *args, **kwargs )
    
    def create ( self, category_slug ):
        instance = self.save ( False )
        if not self.instance:
            self.category = get_object_or_404 ( Category, slug = category_slug )
        instance.save ()
        return instance
    
    def update ( self ):
        return self.save ()

#    def save ( self, commit = True ):
#        if self.category:
#            self.instance.category = self.category
#        self.instance.user = self.user
#        return super ( TopicForm, self ).save ( commit )
    
class ReplyCreationForm ( forms.ModelForm ):
    class Meta:
        model = Reply
        fields = ( 'body', 'topic' )
        widgets = {
            'topic' : forms.HiddenInput (),
        }
        
class ReplyChangeForm ( forms.ModelForm ):
    reply = forms.CharField ( widget = forms.widgets.HiddenInput () )
    
    class Meta:
        model = Reply
        fields = ( 'body', )
#        widgets = {
#            'id' : forms.HiddenInput (),
#        }