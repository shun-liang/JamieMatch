from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User)
    city = models.TextField()
    def __str__(self):
        return "User ID: %s; City: %s", user.username, city

class Chef(models.Model):
    user = models.OneToOneField(User)
    address = models.TextField()
    city = models.TextField()
    post_code = models.TextField()
    def __str__(self):
        return "User ID: %s; Address: %s; City: %s, post_code: %s", user.username, address, city, post_code
