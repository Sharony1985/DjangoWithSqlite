from django.db import models

# Create your models here.
class Task(models.Model):
    name_text = models.CharField(max_length=50)
    description_text =  models.CharField(max_length=200)
