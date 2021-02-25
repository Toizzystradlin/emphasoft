from django.db import models

# Create your models here.

class Datauser(models.Model):
    username = models.CharField(max_length=150, blank=True, null=True)
    fio = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True)


class Cities(models.Model):
    city = models.CharField(max_length=150)