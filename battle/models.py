from django.db import models
from django.forms import CharField
from supers.models import Supers
from super_types.models import SuperType

# Create your models here.

class Battle(models.Model):
  super_one = models.ForeignKey(Supers, on_delete=models.SET_NULL, null=True)
  super_two = models.ForeignKey(SuperType, on_delete=models.SET_NULL, null =True)
  battle_date = models.DateTimeField()
  