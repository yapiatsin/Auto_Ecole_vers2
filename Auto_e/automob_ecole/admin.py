from django.contrib import admin
from .models import * 

class EnginAdmin(admin.ModelAdmin):
    list_display = ('immatriculation','marque','modele','annee_fabrication','date_achat','prix_achat','moniteur_responsable')
    list_filter =('immatriculation','marque','moniteur_responsable')

class EleveAdmin(admin.ModelAdmin):
    list_display = ('nom','prenom','nationalite','ville','permis','commune','equip_visuel','app_auditif','date_inscription','autheur_enreg')
    list_filter =('nom','prenom','autheur_enreg','permis')

#class EnginAdmin(admin.ModelAdmin):
#    list_display = ('immatriculation','marque','modele','annee_fabrication','date_achat','prix_achat','moniteur_responsable')
#    list_filter =('immatriculation','marque','moniteur_responsable')
#
#class EnginAdmin(admin.ModelAdmin):
#    list_display = ('immatriculation','marque','modele','annee_fabrication','date_achat','prix_achat','moniteur_responsable')
#    list_filter =('immatriculation','marque','moniteur_responsable')


admin.site.register(Engin,EnginAdmin)
admin.site.register(Category_engin)
admin.site.register(Eleve, EleveAdmin)
admin.site.register(Moniteur)
admin.site.register(Lecon)
admin.site.register(Reservation)
# Register your models here.
#list_display = ('product','variation_category','variation_value','is_active')
#    list_editable = ('is_active',)
#    list_filter = ('product','variation_category','variation_value','is_active')