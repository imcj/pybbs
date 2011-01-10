#! coding:utf-8
from django.http import HttpResponseRedirect, HttpRequest , HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from pybbs.models import Topic, Reply, Category
from pybbs.forms import TopicForm, ReplyCreationForm, ReplyChangeForm

def topic_list ( request , category_slug, page = 1 ):
    pass

def topic_add ( request ):
    category_slug   = request.GET.get ( "category", request.POST.get ( "category", None ) )
    if "POST" == request.method:
        form = TopicForm ( user = User.objects.get ( pk = 1 ), data = request.POST )
        if form.is_valid ():
            instance = form.create ( category_slug )
    else:
        form = TopicForm ( category_slug = category_slug )
    
    context = {
        "form" : form
    }
    try:
        if instance:
            context['topic'] = instance
    except NameError:
        pass
    
    return render_to_response (
        'pybbs/topic_add.html',
        context,
        context_instance = RequestContext ( request )
    )
    
    
def topic_update ( request ):
    topic_id     = request.GET.get ( "topic", request.POST.get ( "topic", None ) )
    topic_object = get_object_or_404 ( Topic, id = topic_id )

    if "POST" == request.method:
        form = TopicForm ( user = User.objects.get ( pk = 1 ), data = request.POST, instance = topic_object )
        if form.is_valid ():
            instance = form.update ()
    else:
        form = TopicForm ( instance = topic_object )
    
    context = {
        "form" : form
    }
    try:
        if instance:
            context['topic'] = instance
    except NameError:
        pass
    
    return render_to_response (
        'pybbs/topic_update.html',
        context,
        context_instance = RequestContext ( request )
    )
    
def topic ( request, category_slug, topic_id, topic_slug, page = 1 ):
    try:
        topic_object = Topic.objects.read ( topic_slug, topic_id )
    except Topic.DoesNotExist:
        raise Http404
    reply_objects = Reply.objects.list ( topic_object, page )
    
    context = {
        'topic'   : topic_object,
        'replies' : reply_objects
    }
    
    return render_to_response (
        'pybbs/topic.html',
        context,
        context_instance = RequestContext ( request )
    )
    
def reply_add ( request ):
    topic_id     = request.GET.get ( "topic", request.POST.get ( "topic", None ) )
    topic_object = get_object_or_404 ( Topic, pk = topic_id )

    context = {}
    
    if "POST" == request.method:
        reply_new = Reply ( user = User.objects.get ( pk = 1 ), topic = topic_object )
        form = ReplyCreationForm ( data = request.POST, instance = reply_new )
        if form.is_valid ():
            instance = form.save ()
            context['reply'] = instance
    else:
        form = ReplyCreationForm ( initial = { 'topic' : topic_id } )
    
    context['form'] = form
    return render_to_response (
        'pybbs/reply_add.html',
        context,
        context_instance = RequestContext ( request )
    )
    
def reply_update ( request ):
    reply_id     = request.GET.get ( "reply", request.POST.get ( "reply", None ) )
    reply_object = get_object_or_404 ( Reply, pk = reply_id )

    if "POST" == request.method:
        form = ReplyChangeForm ( request.POST, instance = reply_object )
        if form.is_valid ():
            instance = form.save ()
    else:
        form = ReplyChangeForm ( initial = { 'reply' : reply_id }, instance = reply_object )
    
    context = {
        "form" : form
    }
    try:
        if instance:
            context['reply'] = instance
    except NameError:
        pass
    
    return render_to_response (
        'pybbs/reply_update.html',
        context,
        context_instance = RequestContext ( request )
    )