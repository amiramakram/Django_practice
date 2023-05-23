from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from Day2.login.form import CreateLoginForm
from .form import *

from students.models import Student
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET', 'POST'])
def loginFrom(req):
    context = {}
    if(req.method == "POST"):
        email = req.POST['email']
        password = req.POST['password']
        user = Student.objects.filter(email=email, password=password)
        auth_user = authenticate(email=email, password=password)

        if(len(user) == 1 and auth_user):

            req.session["username"] = user[0].username
            req.session["login"] = True
            login(req, auth_user)
            return HttpResponseRedirect('/student/list')

        elif(len(user) == 1):
            req.session["username"] = user[0].username
            req.session["login"] = True
            return HttpResponseRedirect('/student/list')

        else:
            form = CreateLoginForm()
            context['form'] = form
            context['message'] = "*Wrong Email or Password"
            return render(req,'login/login.html', context)

    else:
        form = CreateLoginForm()
        context['form']=form
        return render(req, 'login/login.html', context)