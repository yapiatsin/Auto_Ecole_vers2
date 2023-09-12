from typing import Any, Dict
from urllib import request
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,CreateView, DeleteView, UpdateView
from django.contrib import messages
from .models import *
from .forms import EleveForm, EleveUpdateForm, EnginForm, MoniteurForm



def login(request):
    return render(request, 'registration/login.html')

def dashboard(request):
    return render(request, 'auto/dashboard.html')

def contact(request):
    return render(request, 'auto/contact.html')

def profil(request):
    return render(request, 'auto/profile.html')

def list_moniteur(request):
    return render(request, 'auto/liste_moniteur.html')

def recu(request):
    return render (request,'auto/recu_inscrit.html')

def prof(request):
    return render (request,'auto/prof.html')




class InscriptionView(CreateView):
    model = Eleve
    form_class = EleveForm
    success_message = 'Inscription effectuée avec succès'
    template_name = 'auto/addeleve.html'
    ordering = ['-date_inscription']
    success_url = reverse_lazy ('addeleve')
     
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response
     
class UpdateleveView(UpdateView): 
    model = Eleve
    form_class = EleveUpdateForm
    success_message = 'Modification effectuée avec succès'
    template_name = 'auto/eleveupdate.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response
    
class listeleveView(ListView):
    model = Eleve
    template_name = 'auto/tableleves.html'
    template_name_1 = 'auto/index.html'
    context_object = 'listelev'
    #Pour compter le nombre d'élève enregistrer je vais créé une fonction  
    def get_context_data(self, **kwargs):
        #Definir la variable a qui sera affecter le comptage (context)
        context = super().get_context_data(**kwargs)
        #affecter le compteur a nb_eleve qui la variable qu'on va mettre dans le HTML
        context['nb_eleve'] = self.get_queryset().count()
        #retourner context
        return context

class detaileleveView(DetailView):
    model = Eleve
    template_name = 'auto/elevedetail.html'
    
class deleteleveView(DeleteView):
    model = Eleve
    template_name = 'auto/elevedelete.html'
    success_url = reverse_lazy('listelev')


class AddEnginView(CreateView):
    model         = Engin
    form_class    = EnginForm
    success_message = 'Enregistrement effectué avec succès'
    template_name = 'auto/addengin.html'
    success_url = reverse_lazy ('add_engin')
    
    def form_valid(self, form):
        reponse =  super().form_valid(form)
        messages.success(self.request, self.success_message)
        return reponse
    
    
class AddMoniteurView(CreateView):
    model         = Moniteur
    form_class    = MoniteurForm
    success_message = 'Enregistrement effectué avec succès'
    template_name = 'auto/addmoniteur.html'
    success_url = reverse_lazy ('add_engin')
    
    def form_valid(self, form):
        reponse =  super().form_valid(form)
        messages.success(self.request, self.success_message)
        return reponse
   
class listeMoniteurView(ListView):
    model = Moniteur
    template_name = 'auto/tablemoniteur.html'
    context_object = 'liste_monit'
    #Pour compter le nombre d'élève enregistrer je vais créé une fonction  
    def get_context_data(self, **kwargs):
        #Definir la variable a qui sera affecter le comptage (context)
        context = super().get_context_data(**kwargs)
        #affecter le compteur a nb_eleve qui la variable qu'on va mettre dans le HTML
        context['nb_moniteur'] = self.get_queryset().count()
        #retourner context
        return context 
    
    
    
    
    