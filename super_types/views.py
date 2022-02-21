from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperTypeSerializer
from .models import SuperType
from django.shortcuts import get_object_or_404



@api_view(['GET', 'POST'])
def super_type(request):
  if request.method == 'GET':
    supers_types = SuperType.objects.all()
    serializer = SuperTypeSerializer(supers_types, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = SuperTypeSerializer(data=request.data, status=201)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def super_type_detail(request, pk):

      supertype = get_object_or_404(SuperType, pk=pk)
      if request.method == 'GET':
        serializer = SuperTypeSerializer(supertype);
        return Response(serializer.data)
      elif request.method == "PUT":
        serializer = SuperTypeSerializer(supertype, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
      elif request.method == 'DELETE':
        supertype.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)