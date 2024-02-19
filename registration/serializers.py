from rest_framework import serializers

from .models import Laptop, LaptopMovement, Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = '__all__'
        
class LaptopMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaptopMovement
        fields = '__all__'