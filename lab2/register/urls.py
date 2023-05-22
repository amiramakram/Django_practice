from django.urls import path, include
from register.views import *


urlpatterns = [
    path('', registerForm, name='register')
]
