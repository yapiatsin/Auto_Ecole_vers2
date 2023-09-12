from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


# Create your models here.
class Eleve(models.Model):
    
    HAND_CHOICES = (
        ('Oui','OUI'),
        ('Non','NON'), 
    )
    VIS_CHOICES = (
        ('Oui','OUI'),
        ('Non','NON'), 
    )
    AUD_CHOICES = (
        ('Oui','OUI'),
        ('Non','NON'), 
    )
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True, upload_to='inscription')
    email = models.EmailField(max_length=100, null=True)
    equip_visuel = models.CharField(max_length=3, choices=VIS_CHOICES)
    app_auditif = models.CharField(max_length=3, choices=AUD_CHOICES)
    handicap = models.CharField(max_length=3, choices=HAND_CHOICES)
    date_naissance = models.DateTimeField()
    permis = models.CharField(max_length=4)
    nationalite = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    date_inscription = models.DateField(auto_now_add=True)
    autheur_enreg = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom + ' | ' +str(self.autheur_enreg)
    def get_absolute_url(self):
        return reverse("addeleve")
    @property
    def get_count(self):
        return Eleve.objects.count()
    
    
class Moniteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True, upload_to='moniteur')
    date_naissance = models.DateField()
    email = models.EmailField(max_length=100, null=True)
    nationalite = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    date_embauche = models.DateField()
    salaire = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    autheur_enreg = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.prenom} {self.nom}"
    def get_absolute_url(self):
        return reverse("add_moniteur")
    
    

class Category_engin(models.Model):
    nom_category = models.CharField(max_length=100)
    commtentaire_category = RichTextField(blank=True, null=True)

class Engin(models.Model):
    immatriculation = models.CharField(max_length=15)
    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)
    annee_fabrication = models.PositiveIntegerField()
    date_achat = models.DateField()
    prix_achat = models.DecimalField(max_digits=10, decimal_places=2)
    category_engin = models.ForeignKey(Category_engin, on_delete=models.SET_NULL, null=True)
    moniteur_responsable = models.ForeignKey(Moniteur, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.immatriculation
    def get_absolute_url(self):
        return reverse("add_engin")
    
    
class Reservation(models.Model):
    #eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Engin, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField()
    duree = models.DurationField()
    def __str__(self):
        return f"Réservation de {self.eleve} pour {self.duree}"
    
class Lecon(models.Model):
    #eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    moniteur = models.ForeignKey(Moniteur, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Engin, on_delete=models.CASCADE)
    date_lecon = models.DateTimeField()
    duree = models.DurationField()
    note = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    def __str__(self):
        return f"Leçon de {self.eleve} avec {self.moniteur} le {self.date_lecon}"

    