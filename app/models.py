from django.db import models

# Create your models here.
class users(models.Model):
    login = models.TextField()
    password = models.TextField()



