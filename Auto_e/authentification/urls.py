from django.urls import path
from .views import UserCreationView


urlpatterns = [
    path('compte/', UserCreationView.as_view(), name="cre_compte"),
    #path('detaileleve/<int:pk>', detaileleveView.as_view(), name="detaileleve"),
    #path('eleve_add/', InscriptionView.as_view(), name="addeleve"),
    #path('eleve/editer/<int:pk>', UpdateleveView.as_view(), name="eleve_edite"),
    #path('eleve/<int:pk>/delete', deleteleveView.as_view(), name="eleve_delete"),
    #path('contact', views.contact, name="contact"),
    #path('profil', views.profil, name="user-profil"),
    
    
]

