from rest_framework import viewsets
from .models import Student, Laptop, LaptopMovement
from .serializers import StudentSerializer, LaptopSerializer, LaptopMovementSerializer

"""  a viewset is a class that defines the CRUD (create, read, update, delete) operations that can be performed on a model using the API """ 

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class LaptopViewSet(viewsets.ModelViewSet):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
    
class LaptopMovementViewSet(viewsets.ModelViewSet):
    queryset = LaptopMovement.objects.all()
    serializer_class = LaptopMovementSerializer 