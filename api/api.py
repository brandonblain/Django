from rest_framework.generics import ListCreateAPIView

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import UserSerializers, ProductSerializer

from services.models import Products


class UserAPI(APIView):
    def post(self, request):
        serializer = UserSerializers(data = request.data)
        if(serializer.is_valid()):
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ProductsListAPI (ListCreateAPIView):
    serializer_class = ProductSerializer 
    queryset = Products.objects.all()            
