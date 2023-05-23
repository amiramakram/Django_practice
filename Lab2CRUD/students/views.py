# It Works
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
                      
# def deleteview(req,id):
#     Student.objects.filter(id=id).delete()
#     context={}
#     context['students']=Student.objects.all()
#     return render(req, 'student/list.html', context)

def deleteview(req, id):
    student = Student.objects.get(id=id)
    student.delete()
    # context={}
    # context['students']=Student.objects.all()
    return redirect('student:liststudentname')
    # return render(req, 'student/list.html', context)

def editview(req, id):
    if req.method == 'GET':
        student = Student.objects.get(id=id)
        supervisors = Stuff.objects.all()
        context = {
            'student': student,
            'stuff': supervisors,
        }
        return render(req, 'student/edit.html', context)
    else:
        student = Student.objects.get(id=id)
        student.name = req.POST['studentname']
        student.track = req.POST['trackname']
        student.supervisor_id = req.POST['stuffid']
        student.save()
        return redirect('/students/')

def list(req):
    context={}
    context['students']=Student.objects.all()
    return render(req, 'student/list.html', context)

def addstudent(req):
    if(req.method=="GET"):  
       supervisors=Stuff.objects.all()  
       return render(req,'student/add.html',{'stuff':supervisors})
    else:
        Student.objects.create(
            name=req.POST['studentname'],
            track = req.POST['trackname'],
            supervisor=Stuff.objects.get(id=req.POST['stuffid'])
        )
        return redirect('/students/')

    