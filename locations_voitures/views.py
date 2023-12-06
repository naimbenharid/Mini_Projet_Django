from django.views.generic import ListView,DetailView
from locations_voitures.models import Voiture


# Create your views here.
class VoitureListView(ListView):
    model = Voiture
    template_name = 'locations_voitures/voiture/list.html' 
    context_object_name = 'voitures'

class VoitureDetailView(DetailView):
        model = Voiture
        template_name = 'locations_voitures/voiture/detail.html'  
        context_object_name = 'voiture' 