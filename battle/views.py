from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BattleSerializer
from .models import Battle
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def battle_type(request):
  if request.method == 'GET':
    battles = Battle.objects.all()
    serializer = BattleSerializer(battles, many=True)
    return Response(serializer.data)

  elif request.method == "POST":
    serializer = BattleSerializer(data=request.data)
    serializer.is_valid(raise_exception =True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
