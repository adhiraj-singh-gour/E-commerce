from django.db import models

# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)
    Message = models.CharField(max_length=200)