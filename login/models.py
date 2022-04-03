from django.db import models

class login(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=20,default='pending')
    type = models.CharField(max_length=2)
