from django.views.generic import ListView, DetailView , UpdateView ,DeleteView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from locations_voitures.forms import ReservationForm
from locations_voitures.models import Voiture, Location
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .forms import LocationUpdateForm
# Create your views here.

class VoitureListView(ListView):
    model = Voiture
    template_name = 'locations_voitures/voiture/list.html'
    context_object_name = 'voitures'

class VoitureDetailView(DetailView):
    model = Voiture
    template_name = 'locations_voitures/voiture/detail.html'
    context_object_name = 'voiture'
class UpdateReservationView(UpdateView):
    model = Location
    template_name = 'locations_voitures/voiture/update_reservation.html'
    form_class = LocationUpdateForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        return obj

    def get_success_url(self):
        return reverse_lazy('locations_voitures:update_reservation', kwargs={'pk': self.object.pk})


class DeleteReservationView(DeleteView):
    model = Location
    template_name = 'locations_voitures/voiture/delete_reservation.html'  

    def get_success_url(self):
        return reverse_lazy('locations_voitures:user_reservations')  



@login_required
def reserver_voiture(request, voiture_id):
    voiture = get_object_or_404(Voiture, pk=voiture_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.voiture = voiture
            location.user = request.user
            location.save()

            return redirect('locations_voitures:user_reservations')

    else:
        form = ReservationForm()

    return render(request, 'locations_voitures/voiture/reserver_voiture.html', {'voiture': voiture, 'form': form})
@login_required
def user_reservations(request):
    reservations = Location.objects.filter(user=request.user)
    return render(request, 'locations_voitures/voiture/user_reservations.html', {'reservations': reservations})

def reservation_confirmed(request):
    user_reservations_url = reverse('locations_voitures:user_reservations')

    messages.success(request, f"Redirection vers {user_reservations_url}")

    return render(request, 'locations_voitures/voiture/reservation_confirmed.html', {'user_reservations_url': user_reservations_url})