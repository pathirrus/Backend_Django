from django.db import models

# Create your models here.
class Task(models.Model):
    text = models.TextField()
   # priority = models.IntegerField()

    def __str__(self):
        return f"{self.text}"