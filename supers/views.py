

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Supers
from django.shortcuts import get_object_or_404




@api_view(['GET', 'POST'])
def supers_list(request):

  hero_param = request.query_params.get('type')
  
  supers = Supers.objects.all()

  if hero_param:
    supers = supers.filter(super_type_id__type=hero_param)

    serializer = SuperSerializer(supers, many=True)
    return Response(serializer.data)

   
  if request.method == 'GET':
    supers = Supers.objects.all()
    serializer = SuperSerializer(supers, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = SuperSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

 
@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):

      super = get_object_or_404(Supers, pk=pk)
      if request.method == 'GET':
        serializer = SuperSerializer(super);
        return Response(serializer.data)
      elif request.method == "PUT":
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
      elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   



