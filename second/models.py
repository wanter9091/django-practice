from django.db import models

# Create your models here.

class Item(models.Model):
    human=models.CharField(max_length=200)