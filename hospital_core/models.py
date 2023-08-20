from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self) -> str:
        return f"Department -> {self.name}"

class Room(models.Model):
    number = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Room No -> {self.number}"