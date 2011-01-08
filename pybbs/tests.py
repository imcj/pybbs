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