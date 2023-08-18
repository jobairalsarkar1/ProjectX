from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200)

class Room(models.Model):
    number = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
