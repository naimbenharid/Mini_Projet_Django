from django import forms
from .models import Location
from django.contrib import messages

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['date_debut', 'date_fin', 'nombres_jours']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ajoutez d'autres personnalisations au besoin

    def clean(self):
        cleaned_data = super().clean()
        date_debut = cleaned_data.get("date_debut")
        date_fin = cleaned_data.get("date_fin")

        # Vérifier si la date de début est antérieure à la date de fin
        if date_debut and date_fin and date_debut >= date_fin:
            raise forms.ValidationError("La date de début doit être antérieure à la date de fin")

        return cleaned_data




class LocationUpdateForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['voiture', 'date_debut', 'date_fin']

        def form_valid(self, form):
            response = super().form_valid(form)
            messages.success(self.request, 'Votre réservation a été mise à jour avec succès.')
            return response