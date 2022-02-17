from django.db import models
from django.forms import CharField

# Create your models here.

class SuperType(models.Model):
    type = CharField(max_length=255)