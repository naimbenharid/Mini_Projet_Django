from django.contrib import admin

from locations_voitures.models import Location, Voiture, VoitureImage

# Register your models here.
@admin.register(Voiture)
class VoitureAdmin(admin.ModelAdmin):
    list_display = ('marque', 'modele', 'annee_fabrication', 'couleur', 'immatriculation')
    search_fields = ('marque', 'modele', 'immatriculation')



@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'voiture', 'date_debut', 'date_fin', 'prix_jour','nombres_jours','total')
    search_fields = ('client__nom', 'voiture__marque', 'utilisateur__username')

@admin.register(VoitureImage)
class VoitureImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'voiture')