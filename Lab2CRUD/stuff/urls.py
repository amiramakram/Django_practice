from django.urls import path

from .views import *
app_name = 'stuff'

urlpatterns = [
    path('', list, name='listsupervisorname'),
    path('insert/', insert, name='insert'),
    path('delete/<int:id>',deleteview,name='superdelete'),
    path('update/<int:id>',editview,name='superedit')
]
