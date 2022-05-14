from django.db import models
from login.models import login

class partnerreg(models.Model):
    pid = models.OneToOneField(login,on_delete=models.CASCADE,primary_key=True)
    sname = models.CharField(max_length=50)
    oname = models.CharField(max_length=50) 
    email = models.EmailField(max_length=100)
    phone =models.CharField(max_length=10)
    address = models.CharField(max_length=250)
    license = models.CharField(max_length=60)