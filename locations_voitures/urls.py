from django.urls import path
from . import views
from .views import VoitureListView, VoitureDetailView

app_name='locations_voitures' #define application namespace

#domain.com/blog/...
urlpatterns=[
    path('',views.VoitureListView.as_view(), name='voiture_list'),
    path('<int:id>/',views.VoitureDetailView.as_view(),name='voiture_detail'),
]