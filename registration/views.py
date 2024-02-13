from rest_framework import viewsets
from .models import School, Student, Laptop, LaptopRegistration, TheftReport
from .serializers import SchoolSerializer, LaptopSerializer, LaptopRegistrationSerializer, TheftReportSerializer, StudentSerializer

"""  a viewset is a class that defines the CRUD (create, read, update, delete) operations that can be performed on a model using the API """ 


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class LaptopViewSet(viewsets.ModelViewSet):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
    
class LaptopRegistrationViewSet(viewsets.ModelViewSet):
    queryset = LaptopRegistration.objects.all()
    serializer_class = LaptopRegistrationSerializer
    
class TheftReportViewSet(viewsets.ModelViewSet):
    queryset = TheftReport.objects.all()
    serializer_class = TheftReportSerializer