from django.db import models

class UserRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=250, unique=True) 
    password = models.CharField(max_length=150) 
    date_registered = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"