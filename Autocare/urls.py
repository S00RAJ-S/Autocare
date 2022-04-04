from django.urls import path,include

urlpatterns = [
    path('', include('login.urls')),
    path('registration/',include('user.urls')),
    path('admin/',include('admin.urls')),
    path('user/',include('user.urls')),
    path('partner/',include('partner.urls')),
]
