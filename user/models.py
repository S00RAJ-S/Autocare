from django.db import models
from login.models import login

class userreg(models.Model):
    uid = models.OneToOneField(login,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=50) 
    email = models.EmailField(max_length=100)
    phone =models.CharField(max_length=10)
    address = models.CharField(max_length=250)