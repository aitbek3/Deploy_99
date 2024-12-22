from rest_framework import serializers
from .models import Laptop, LaptopPhoto

class LaptopPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaptopPhoto
        fields = '__all__'

class LaptopSerializer(serializers.ModelSerializer):
    photos = LaptopPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Laptop
        fields = '__all__'
