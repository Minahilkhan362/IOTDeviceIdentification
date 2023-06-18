from django.db import models


class AppUser(models.Model):
    username = models.CharField(max_length=50, null=False, unique=True)
    password = models.CharField(max_length=50, null=False)
