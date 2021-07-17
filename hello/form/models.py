from django.db import models

# Create your models here.

class Message(models.Model):
    CHOICES = [
        ("question", "Pytanie"),
        ("other", "INNE")
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    category = models. CharField(max_length=10, choices =CHOICES)
    subject = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f"{self.subject} od {self.name}"