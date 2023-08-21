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

class Notification(models.Model):
    sender_id = models.PositiveIntegerField()
    receiver_id = models.PositiveIntegerField()
    sent_by_patient = models.BooleanField(default=False)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def is_sender_patient(self):
        return self.sent_by_patient