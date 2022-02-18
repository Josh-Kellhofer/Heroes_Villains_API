from rest_framework import serializers
from .models import SuperType

class SuperSerializer(serializers.ModelSerializer):
  class Meta:
    model = SuperType
    fields = ['id','type']
    depth = 1

  super_type_id = serializers.IntegerField(write_only=True)