from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=100)
    date = models.CharField(max_length=10)

    def __str__(self):
        return self.name