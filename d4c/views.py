# Create your views here.
from django.http import HttpResponse,HttpResponsePermanentRedirect
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext
import json
from django.conf import settings
from d4c.models import *
#custom libraries
def value_from_req(request,key,default):
    value = getattr(request, 'GET').get(key)
    if not value:
        value = getattr(request, 'POST').get(key)
    if not value:
        return default
    return value

def home(request):
    return render_to_response('index.html',locals(),context_instance=RequestContext(request))

def form_handler(request):
    data = value_from_req(request,'data',{})
    form = FormRequest()
    form.data = data
    form.save()