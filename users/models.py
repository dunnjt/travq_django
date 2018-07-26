from django.db import models
import uuid
from djongo import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, primary_key=True)
    name = models.TextField(blank=True)
    password = models.TextField(blank=True)
    points = models.IntegerField(blank=True)
    email = models.TextField(blank=True)

class Tag(models.Model):
    tag = models.TextField(blank=True)

class Question(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField(blank=True)
    createdOn = models.DateTimeField(default=timezone.now, blank=True)
    tag = models.ManyToManyField(Tag)

class Answer(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.TextField(blank=True)
    votes = models.IntegerField(blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    createdOn = models.DateTimeField(default=timezone.now, blank=True)

class Skill(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.TextField(blank=True)

class Badge(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.TextField(blank=True)
