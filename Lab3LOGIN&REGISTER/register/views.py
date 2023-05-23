from django.shortcuts import render
from Day2.register.form import CreateRegisterForm

import students.views
from stuff.models import *
from students.models import *
from students.views import *
from .form import *
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET', 'POST'])
def registerForm(req):
    if req.method == 'GET':
        context = {'staff': Stuff.objects.all()}
        context['form']=CreateRegisterForm()
        return render(req, 'register/register.html', context)
    else:
        if Stuff.objects.filter(email=req.POST['email']).exists():
            context = { 'message': 'Email already exists' }
            context['form'] = CreateRegisterForm()
            return render(req, 'register/register.html', context)
        else:
            Student.objects.create(
                username=req.POST['username'],
                address=req.POST['address'],
                email=req.POST['email'],
                password=req.POST['password'],
                staff_id=Stuff.objects.get(id=req.POST['staff_id']))
            return students.views.insertStudent(req)