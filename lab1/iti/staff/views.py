from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect

# Create your views here.
def index(req):
    res = HttpResponse('staff view list')
    return res

def create(req):
    return JsonResponse({'id':1,'name':'Eng/ahmed','courses':['c#','.net']})


def update(req):
    return JsonResponse({'id':1,'name':'Eng/ahmed','courses':['PHP','Laravel']})


def delete(req):
    return  HttpResponseRedirect('/staff/')