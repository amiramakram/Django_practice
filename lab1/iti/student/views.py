from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect

# Create your views here.
def index(req):
    res = HttpResponse('student view list')
    return res

def create(req):
    return  render(req,'student/insert.html')

def update(req):
    return  render(req,'student/update.html')

def delete(req):
    return  HttpResponseRedirect('/student/')