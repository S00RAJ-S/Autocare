from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('home/',views.home),
    path('submit/',views.submit),
    path('submitbooking/',views.submitbooking),
    path('mybookings/',views.mybookings),
    path('delbooking/',views.delbooking),
    path('viewoffers/',views.viewoffers),
    path('acceptoffer/',views.acceptoffer),
]
