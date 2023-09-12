from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm


class UserCreationView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_message = 'Votre compte à été créer avec success'
    success_url = reverse_lazy('cre_compte')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response
    
    
    
# Create your views here.


