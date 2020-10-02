from django.db import models

# Create your models here.
class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length = 20)
    password2 = models.CharField(max_length = 20)