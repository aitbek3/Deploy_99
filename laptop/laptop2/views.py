from rest_framework import viewsets
from .models import Laptop, LaptopPhoto
from .serializers import LaptopSerializer, LaptopPhotoSerializer

class LaptopViewSet(viewsets.ModelViewSet):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer

class LaptopPhotoViewSet(viewsets.ModelViewSet):
    queryset = LaptopPhoto.objects.all()
    serializer_class = LaptopPhotoSerializer
