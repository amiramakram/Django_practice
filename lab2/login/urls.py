from django.urls import path, include
from login.views import *


urlpatterns = [
    path("", loginFrom, name='login')
]