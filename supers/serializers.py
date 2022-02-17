from rest_framework import serializers
from .models import Supers

class SuperSerializer(serializers.ModelSerializer):
  class Meta:
    model = Supers
    fields = ['name,' 'alter_ego', 'primary ability', 'secondary_ability', 'catchphrase', 'super_type']