from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import SuperType




@api_view(['GET' 'POST'])
def super_type(request):
  if request.method == 'GET':
    supers = SuperType.objects.all()
    serializer = SuperSerializer(supers, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = SuperSerializer(data=request.data, status=201)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)