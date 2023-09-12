from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime, date
from django.shortcuts import render
from django.utils import timezone

class SignUpForm(UserCreationForm):
    email =forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email...'}))
    nom = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Nom...'}),)
    prenom = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Prenoms...'}),)
    date_naissance = forms.DateTimeField(widget= forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control','placeholder':'Selection une date...', 'format':'yyyy-mm-dd', 'type':'date'}))

    class Meta:
        model = User
        fields = ('username','nom','prenom','date_naissance','email','password1','password2')
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget  = forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Nom utilisateur....'})
        self.fields['password1'].widget = forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Mot de passe(contenir au moins 8 caractères alpha-numeric)....'})
        self.fields['password2'].widget = forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Confirme mot de passe....'})
        
