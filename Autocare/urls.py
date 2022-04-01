from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('login/', include('login.urls')),
    path('registration/',include('user.urls')),
]
