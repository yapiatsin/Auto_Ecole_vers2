from django import forms
from .models import Eleve, Engin, Moniteur

class EleveForm(forms.ModelForm):
    date_naissance = forms.DateTimeField(widget= forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control','placeholder':'Selection une date...', 'format':'yyyy-mm-dd', 'type':'date'}))
    class Meta:
        model = Eleve
        fields = ('nom','prenom','email','date_naissance','photo','handicap','equip_visuel','app_auditif','permis','nationalite','ville','commune','quartier','telephone','autheur_enreg')

        widgets = {
            'nom': forms.TextInput(attrs={'class':'form-control','placeholder':'Nom...'}),
            'prenom': forms.TextInput(attrs={'class':'form-control','placeholder':'Prenoms...'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email...'}),
            'equip_visuel':forms.Select(attrs={'class':'form-control'}),
            'app_auditif' :forms.Select(attrs={'class':'form-control'}),
            'handicap'    :forms.Select(attrs={'class':'form-control'}),
            'photo': forms.FileInput(attrs={'class':'form-control'}),
            'nationalite': forms.TextInput(attrs={'class':'form-control','placeholder':'nationalite...'}),
            'permis': forms.TextInput(attrs={'class':'form-control','placeholder':'Permis...'}),
            'ville': forms.TextInput(attrs={'class':'form-control','placeholder':'Ville...'}),
            'commune': forms.TextInput(attrs={'class':'form-control','placeholder':'Commune...'}),
            'quartier': forms.TextInput(attrs={'class':'form-control','placeholder':'Quartier...'}),
            'telephone': forms.TextInput(attrs={'class':'form-control','placeholder':'Numero...'}),
            'autheur_enreg': forms.Select(attrs={'class':'form-control'}),
        }
        

class EleveUpdateForm(forms.ModelForm):
    date_naissance = forms.DateTimeField(widget= forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control','placeholder':'Selection une date...', 'format':'yyyy-mm-dd', 'type':'date'}))
    class Meta:
        model = Eleve
        fields = ('nom','prenom',"photo",'email','date_naissance','equip_visuel','app_auditif','handicap','permis','nationalite','ville','commune','quartier','telephone','autheur_enreg')
        widgets = {
            'nom': forms.TextInput(attrs={'class':'form-control','placeholder':'Nom'}),
            'prenom': forms.TextInput(attrs={'class':'form-control','placeholder':'Prenoms'}),
            'date_naissance': forms.DateTimeInput(attrs={'class':'form-control'}),
            'photo': forms.FileInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email...'}),
            'equip_visuel':forms.Select(attrs={'class':'form-control'}),
            'app_auditif' :forms.Select(attrs={'class':'form-control'}),
            'handicap'    :forms.Select(attrs={'class':'form-control'}),
            'nationalite': forms.TextInput(attrs={'class':'form-control','placeholder':'nationalite'}),
            'permis': forms.TextInput(attrs={'class':'form-control','placeholder':'Permis'}),
            'ville': forms.TextInput(attrs={'class':'form-control','placeholder':'Ville'}),
            'commune': forms.TextInput(attrs={'class':'form-control','placeholder':'Commune'}),
            'quartier': forms.TextInput(attrs={'class':'form-control','placeholder':'Quartier'}),
            'telephone': forms.TextInput(attrs={'class':'form-control','placeholder':'Numero'}),
            'autheur_enreg': forms.Select(attrs={'class':'form-control'}),
        }

class EnginForm(forms.ModelForm):
    annee_fabrication = forms.DateTimeField(widget= forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control','placeholder':'Selection une date...', 'format':'yyyy-mm-dd', 'type':'date'}))
    date_achat = forms.DateTimeField(widget= forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control','placeholder':'Selection une date...', 'format':'yyyy-mm-dd', 'type':'date'}))
    class Meta:
        model = Engin
        fields = ('immatriculation','marque','modele','annee_fabrication','date_achat','prix_achat','category_engin','moniteur_responsable')

        widgets = {
            
            'immatriculation': forms.TextInput(attrs={'class':'form-control','placeholder':'Immatriculation...'}),
            'marque': forms.TextInput(attrs={'class':'form-control','placeholder':'Marque...'}),
            'modele': forms.EmailInput(attrs={'class':'form-control','placeholder':'Modele...'}),
            'annee_fabrication':forms.DateTimeInput(attrs={'class':'form-control'}),
            'date_achat':forms.DateTimeInput(attrs={'class':'form-control'}),
            'prix_achat' :forms.NumberInput(attrs={'class':'form-control'}),
            'category_engin'    :forms.Select(attrs={'class':'form-control'}),
            #'photo': forms.FileInput(attrs={'class':'form-control'}),
            'moniteur_responsable': forms.Select(attrs={'class':'form-control','placeholder':'moniteur_responsable...'}),
           
        }
       


class MoniteurForm(forms.ModelForm):
    date_naissance = forms.DateTimeField(widget= forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control','placeholder':'Selection une date...', 'format':'yyyy-mm-dd', 'type':'date'}))
    date_embauche = forms.DateTimeField(widget= forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control','placeholder':'Selection une date...', 'format':'yyyy-mm-dd', 'type':'date'}))
    class Meta:
        model = Moniteur
        fields = ('nom','prenom','email','photo','date_naissance','salaire','date_embauche','nationalite','ville','commune','quartier','telephone','autheur_enreg')

        widgets = {
            'nom': forms.TextInput(attrs={'class':'form-control','placeholder':'Nom...'}),
            'prenom': forms.TextInput(attrs={'class':'form-control','placeholder':'Prenoms...'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email...'}),
            'photo': forms.FileInput(attrs={'class':'form-control'}),
            'nationalite': forms.TextInput(attrs={'class':'form-control','placeholder':'nationalite...'}),
            'salaire': forms.NumberInput(attrs={'class':'form-control','placeholder':'Salaire...'}),
            'ville': forms.TextInput(attrs={'class':'form-control','placeholder':'Ville...'}),
            'commune': forms.TextInput(attrs={'class':'form-control','placeholder':'Commune...'}),
            'quartier': forms.TextInput(attrs={'class':'form-control','placeholder':'Quartier...'}),
            'telephone': forms.TextInput(attrs={'class':'form-control','placeholder':'Numero...'}),
            'autheur_enreg': forms.Select(attrs={'class':'form-control'}),
        }
        



