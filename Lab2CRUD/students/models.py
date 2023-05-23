from django.db import models
from stuff.models import *

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    name = models.CharField(max_length=50)
    track = models.CharField(max_length=100)
    supervisor =models.ForeignKey(to='stuff.Stuff',on_delete=models.CASCADE)