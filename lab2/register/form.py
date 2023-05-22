from django import forms
from stuff.models import *

class CreateRegisterForm(forms.Form):
    username = forms.CharField(max_length=30, required=True,label='Username',widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=50, required=True,label='Address',widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=25, required=True, label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=30, label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    staff_id = forms.ChoiceField(required=True, label='Staff',choices=[(stf.id, stf.username) for stf in Stuff.objects.all()])