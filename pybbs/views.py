#! coding:utf-8
from django.http import HttpResponseRedirect , HttpRequest , HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from pybbs.models import Topic, Reply
from pybbs.forms import TopicForm

def topic_list ( request , category_slug, page = 1 ):
    pass

def topic_add ( request ):
    category_slug = request.GET.get ( "category", None )
    if not category_slug:
        raise Http404 ()

    if "POST" == request.method:
        form = TopicForm ( request.POST )
    else:
        form = TopicForm ()
    
    context = {
        "form" : form
    }
    
    return render_to_response (
        'pybbs/topic_add.html',
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