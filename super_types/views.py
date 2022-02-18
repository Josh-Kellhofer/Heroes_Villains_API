from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperSerializer
from .models import SuperType




@api_view(['GET'])
def super_type(request):
  supers = SuperType.objects.all()
  
  serializer = SuperSerializer(supers, many=True)
  return Response(serializer.data)
