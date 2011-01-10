#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

from django.test import TestCase
from django.test.client import Client
from pybbs.models import Topic, Reply
import django

class ModelTest ( TestCase ):
    
    fixtures = [ 'initial_data' ]
    
    def test_topic_read ( self ):
        try:
            topic_object = Topic.objects.read ( "hello", 1 )
        except Topic.DoesNotExist:
            topic_object = None
        self.assertEqual ( isinstance ( topic_object, Topic ), True, u"No topic." )
    
    def test_reply_list ( self ):
        topic_object = Topic.objects.read ( "hello", 1 )
        reply_objects = Reply.objects.list ( topic_object )
        self.assertEqual ( isinstance ( reply_objects, django.db.models.query.QuerySet ), True )

class ControllTest ( TestCase ):
    
    fixtures = [ 'initial_data' ]
    
    def setUp ( self ):
        self.client = Client ()
        
    def test_topic ( self ):
        response = self.client.get ( "/d/1-hello/" )
        context = response.context
        self.assertEqual ( response.status_code, 200, u"Topic page." )
        self.assertEqual ( context.has_key ( "topic" ), True )
        self.assertEqual ( context.has_key ( "replies" ), True )
        
    def test_topic_add ( self ):
        response = self.client.post ( "/topic/add.py", {
            "category" : u"python",
            "subject" : u"聊天",
            "slug" : u"talking",
            "body" : u"如题",
        } )
        is_valid = response.context['form'].is_valid ()
        if not is_valid:
            print response.context['form'].errors
        self.assertEqual ( is_valid , True )
        topic_object = response.context['topic']
        topic_object_new = Topic.objects.read ( slug = topic_object.slug, id = topic_object.id )
        
        self.assertEqual ( response.status_code, 200 )
        self.assertEqual ( isinstance ( topic_object_new, Topic ), True )
        
    def test_topic_update ( self ):
        response = self.client.post ( "/topic/update.py", {
            "topic" : 1,
            "subject" : u"聊天",
            "slug" : u"talking",
            "body" : u"如题",
        } )
        is_valid = response.context['form'].is_valid ()
        if not is_valid:
            print response.context['form'].errors
        self.assertEqual ( is_valid , True )
        topic_object = response.context['topic']
        topic_object_new = Topic.objects.read ( slug = topic_object.slug, id = topic_object.id )
        
        self.assertEqual ( response.status_code, 200 )
        self.assertEqual ( isinstance ( topic_object_new, Topic ), True )
        
    def test_reply_add ( self ):
        response = self.client.post ( "/reply/add.py", {
            "topic" : 1,
            "body" : u"顶",
        } )
        is_valid = response.context['form'].is_valid ()
        if not is_valid:
            print response.context['form'].errors
        self.assertEqual ( is_valid , True )
        reply_object = response.context['reply']
        reply_object_new = Reply.objects.get ( id = reply_object.id )
        
        self.assertEqual ( response.status_code, 200 )
        self.assertEqual ( reply_object_new, reply_object )
        self.assertEqual ( reply_object_new.topic.replies, 4 )
        
    def test_reply_update ( self ):
        response = self.client.post ( "/reply/update.py", {
            "reply" : 1,
            "body"  : u"顶",
        } )
        is_valid = response.context['form'].is_valid ()
        if not is_valid:
            print response.context['form'].errors
        self.assertEqual ( is_valid , True )
        reply_object = response.context['reply']
        reply_object_new = Reply.objects.get ( id = reply_object.id )
        
        self.assertEqual ( response.status_code, 200 )
        self.assertEqual ( reply_object_new, reply_object )
        self.assertEqual ( reply_object_new.topic.replies, 3 )