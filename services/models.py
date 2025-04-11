from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=30) 
    email = models.EmailField(max_length=30, unique=True)
    position = models.TextField()

class Signup(models.Model):  
    UserName = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    token = models.CharField(max_length=100,unique=True)
