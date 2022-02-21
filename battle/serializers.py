from rest_framework import serializers
from .models import Battle

class BattleSerializer(serializers.model.Serializer):
  class Meta:
    model = Battle
    fields = ['supe_one', 'supe_two', 'battle_date']