from django.db import models
from datetime import datetime

# Create your models here.
class Guest(models.Model):
    name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length = 254)
    message = models.TextField()
    submission_date = models.DateTimeField(default=datetime.now, blank=True)

