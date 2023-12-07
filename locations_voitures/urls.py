from django.urls import path
from . import views
from .views import VoitureListView, VoitureDetailView, reserver_voiture ,reservation_confirmed, user_reservations ,UpdateReservationView,DeleteReservationView

app_name='locations_voitures' #define application namespace

#domain.com/blog/...

urlpatterns=[
    path('',views.VoitureListView.as_view(), name='voiture_list'),
    path('<int:pk>/',views.VoitureDetailView.as_view(),name='voiture_detail'),
    path('reserver_voiture/<int:voiture_id>/', reserver_voiture, name='reserver_voiture'),
    path('mes_reservations/', user_reservations, name='user_reservations'),
    path('reservation_confirmed/', reservation_confirmed, name='reservation_confirmed'),
    path('update_reservation/<int:pk>/', UpdateReservationView.as_view(), name='update_reservation'),
    path('delete_reservation/<int:pk>/', DeleteReservationView.as_view(), name='delete_reservation'),

]