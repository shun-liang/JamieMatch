from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User)
    city = models.TextField()

class Chef(models.Model):
    user = models.OneToOneField(User)
    address = models.TextField()
    city = models.TextField()
    post_code = models.TextField()
