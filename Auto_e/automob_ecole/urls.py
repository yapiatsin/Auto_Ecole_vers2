from django.urls import path
from .views import AddEnginView, listeleveView, detaileleveView, InscriptionView, UpdateleveView, deleteleveView, AddMoniteurView,listeMoniteurView
from .import views


urlpatterns = [
    
    path('dashboard', views.dashboard, name="dashboard"),
    path('list_moniteur', views.list_moniteur, name="listmoniteur"),
    path('', views.login, name="login"),
    
    
    path('listeleve', listeleveView.as_view(), name="listelev"),
    path('detaileleve/<int:pk>', detaileleveView.as_view(), name="detaileleve"),
    path('eleve_add/', InscriptionView.as_view(), name="addeleve"),
    path('eleve/editer/<int:pk>', UpdateleveView.as_view(), name="eleve_edite"),
    path('eleve/<int:pk>/delete', deleteleveView.as_view(), name="eleve_delete"),
    path('contact', views.contact, name="contact"),
    path('profil', views.profil, name="user-profil"),
    
    
    path('AddEngin', AddEnginView.as_view(), name="add_engin"),
    
    path('recu_inscription', views.recu, name="recu-ins"),
    
    
    
    path('AddMoniteur', AddMoniteurView.as_view(), name="add_moniter"),
    path('listemoniteur', listeMoniteurView.as_view(), name="liste_monit"),
    
    
    
]
