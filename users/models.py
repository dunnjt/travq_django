from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField(blank=True)
    password = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    points = models.IntegerField(blank=True)
    email = models.TextField(blank=True)
    badges = models.TextField(blank=True)
