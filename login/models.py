from django.db import models

class login(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
