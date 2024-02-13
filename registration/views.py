from django.shortcuts import redirect, render
from rest_framework import viewsets

from .models import Laptop, LaptopMovement, Student
from .serializers import (LaptopMovementSerializer, LaptopSerializer,
                          StudentSerializer)

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


def home(request):
    return render(request, "home.html")