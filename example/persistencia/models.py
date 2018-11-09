from django.db import models

# Create your models here.


class Task(models.Model):
    problem = models.CharField(max_length=100)
    status = models.IntegerField(null=False)
    date = models.DateField(null=False)
