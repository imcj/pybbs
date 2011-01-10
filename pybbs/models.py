#! coding:utf-8
from django.db import models
from django.db.models.signals import post_save
from django.db.models import Q
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField ( u'名称',   max_length = 200 )
    slug = models.SlugField ( u"短地址", max_length = 200 )
    topics = models.BigIntegerField ( u'主题', default = 0 )
    replies = models.BigIntegerField ( u'回复', default = 0 )
    
    def __unicode__ ( self ):
        return self.name
    
class TopicManager ( models.Manager ):
    def listWithCategory ( self, category, page = 1 ):
        pass
    
    def read ( self, slug, id ):
        return super ( TopicManager, self ).get_query_set ().get ( Q ( slug = slug ), Q ( id = id ) )

class Topic(models.Model):
    category = models.ForeignKey ( Category )
    user = models.ForeignKey(User)
    slug = models.SlugField ( u"短地址", max_length = 100, null = True, blank = True )
    subject = models.CharField ( u'主题' , max_length = 255 )
    body = models.TextField ( u'内容' )
    visits = models.BigIntegerField ( u'浏览', default = 0, editable = False )
    replies = models.BigIntegerField ( u'回复', default = 0, editable = False )
    create_at = models.DateTimeField ( u'发表时间', auto_now_add = True )
    update_at = models.DateTimeField ( u'最后修改时间', auto_now = True, auto_now_add = True )
    last_reply_author = models.ForeignKey ( User, related_name = 'last_reply_author', null = True, blank = True )
    last_reply_create = models.DateTimeField ( u'最后回复时间', auto_now_add = True, null = True, blank = True )
    
    objects = TopicManager ()
    
    def __unicode__ ( self ):
        return self.subject

class ReplyManager ( models.Manager ):
    def create(self, **kwargs):
        import pdb; pdb.set_trace ()

    def list ( self, topic, page = 1 ):
        return super ( ReplyManager, self ).filter ( topic = topic )

class Reply(models.Model):
    topic = models.ForeignKey ( Topic, verbose_name = u"主题" )
    user = models.ForeignKey ( User )
    body = models.TextField ( u'内容' )
    create_at = models.DateTimeField ( u'发表时间', auto_now_add = True )
    update_at = models.DateTimeField ( u'最后修改时间', auto_now = True, auto_now_add = True )

    objects = ReplyManager () 
    
    class Meta:
        ordering = [ '-create_at' ]

    def __unicode__ ( self ):
        return self.body
    
    def save(self, **kwargs ):
        if self.pk is None:
            topic = self.topic
            topic.replies += 1
            topic.last_reply_create = self.create_at
            topic.last_reply_author = User ( id = self.user.id )
            topic.save ()
            
        super ( Reply, self ).save ( **kwargs )

def post_reply ( sender, instance, raw, created, **kwargs ):
    if instance and created:
        import pdb; pdb.set_trace ()
        topic = instance.topic
        topic.replies += 1
        topic.last_reply_create = instance.create_at
        topic.last_reply_author = instance.user

def post_topic ( sender, instance, raw, created, **kwargs ):
    pass

#post_save.connect ( post_reply, Reply )
post_save.connect ( post_topic, Topic )