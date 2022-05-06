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

class partneroffer(models.Model):
    bid = models.IntegerField()
    pid = models.IntegerField()
    wname = models.CharField(max_length=60)
    wphone = models.IntegerField()
    rate = models.IntegerField()

class order(models.Model):
    oid = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    details = models.CharField(max_length=500)
    category = models.CharField(max_length=20)
    pid = models.IntegerField()
    wname = models.CharField(max_length=60)
    wphone = models.IntegerField()
    rate = models.IntegerField()    