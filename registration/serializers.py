from rest_framework import serializers
from .models import School, Student, Laptop, LaptopRegistration, TheftReport


# serializers are used to convert complex data types, such as Django model instances, into Python data types that can be easily rendered into JSON, XML, or other content types

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = '__all__'
        
class LaptopRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaptopRegistration
        fields = '__all__'
        
class TheftReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheftReport
        fields = '__all__'