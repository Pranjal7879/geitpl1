from django.db import models
class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    position = models.TextField()
# Create your models here.
