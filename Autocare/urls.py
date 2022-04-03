from django.urls import path,include

urlpatterns = [
    path('', include('login.urls')),
    path('registration/',include('user.urls')),
    path('admin/',include('admin.urls'))
]
