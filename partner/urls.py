from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('home/',views.home),
    path('submit/',views.submit),
    path('placeoffer/',views.placeoffer),
    path('submitoffer/',views.submitoffer),
    path('bids/',views.bids),
    path('partnerorders/',views.partnerorder),
]
