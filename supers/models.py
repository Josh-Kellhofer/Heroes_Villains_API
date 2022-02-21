from django.db import models
from django.forms import CharField
from super_types.models import SuperType


# Create your models here.

class Supers(models.Model):
  name = models.CharField(max_length=255, default = "")
  alter_ego = models.CharField(max_length=255, default = "")
  primary_ability = models.CharField(max_length=255, default = "")
  secondary_ability = models.CharField(max_length=255, default = "")
  catchphrase = models.CharField(max_length=255, default = "")
  super_type = models.ForeignKey(SuperType, on_delete=models.SET_NULL, null = True)
