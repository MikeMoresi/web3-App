from django.db import models
from django.conf import settings

# Create your models here.

class Transaction(models.Model):
    sender = models.CharField(max_length=256)
    recipient = models.CharField(max_length=256)
    amount = models.BigIntegerField()
    event = models.CharField(max_length=256)
