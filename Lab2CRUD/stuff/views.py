from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from .models import *

def list(req):
    supervisors = Stuff.objects.all()
    return render(req, 'stuff/list.html', {'stuffs': supervisors})

def insert(req):
    if req.method == "GET":
        return render(req, 'stuff/add.html')
    else:
        Stuff.objects.create(name=req.POST['stuffname'])
        return redirect('/stuff/')

def deleteview(req, id):
    supervisor = Stuff.objects.get(id=id)
    supervisor.delete()
    return redirect('stuff:listsupervisorname')

def editview(req, id):
    supervisor = Stuff.objects.get(id=id)
    if req.method == "GET":
        return render(req, 'stuff/edit.html', {'supervisor': supervisor})
    else:
        supervisor.name = req.POST['stuffname']
        supervisor.save()
        return redirect('/stuff/')


