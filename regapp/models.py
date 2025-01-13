from django.db import models

# Create your models here.

class Register(models.Model):
    Fullname=models.CharField(max_length=200)
    Username=models.CharField(max_length=100)
    Password=models.IntegerField()
    email=models.EmailField()
   
    def __str__(self):
        return f'{self.Fullname} ({self.Username})'
