from django.db import models
from django.forms import CharField
from super_types.models import SuperType

# Create your models here.

class Supers(models.Model):
  name = CharField(max_length=255)
  alter_ego = CharField(max_length=255)
  primary_ability = CharField(max_length=255)
  secondary_ability = CharField(max_length=255)
  catchphrase = CharField(max_length=255)
  super_type = models.ForeignKey(SuperType, on_delete=models.CASCADE)
