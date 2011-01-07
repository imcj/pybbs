#! coding:utf-8
from django.http import HttpResponseRedirect , HttpRequest , HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import User
from org_51py.bbs.models import *

def index(req):
    pass

def category(req , cate):
    pass

def thread(req , id):
    try:
        tid = int(id)
        td = Thread.objects.get(id=id)
        return HttpResponse(td.title)
    except:
        return HttpResponseRedirect('/error/')

def reply(req , tid):
    if( req.method == 'POST' ):
        pass
    else:
        return render_to_response('reply.html' , locals())