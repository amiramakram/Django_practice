from django.urls import path

from .views import *


app_name = 'student'

urlpatterns = [
    path('insert', addstudent, name='addstudentname'),
    path('',list, name='liststudentname'),
    path('delete/<int:id>',deleteview,name='studentdelete'),
    path('update/<int:id>',editview,name='studentedit'),
]

