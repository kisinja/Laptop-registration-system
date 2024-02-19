from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
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


@login_required(login_url="/users/login/")
def home(request):
    checkins_today = LaptopMovement.objects.count()
    students_count = Student.objects.count()
    laptops_count = Laptop.objects.count()

    context = {
        "checkins_today": checkins_today,
        "students_count": students_count,
        "laptops_count": laptops_count
    }

    return render(request, "home.html", context)


@login_required(login_url="/users/login/")
def laptops(request):
    laptops = Laptop.objects.all()

    paginator = Paginator(laptops, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"laptops": laptops, "page_obj": page_obj}
    return render(request, "laptops/laptops.html", context)


@login_required(login_url="/users/login/")
def new_laptop(request):
    if request.method == "POST":
        student = request.POST.get("student")
        serial_number = request.POST.get("serial_number")
        make = request.POST.get("make")
        model = request.POST.get("model")
        color = request.POST.get("color")
        specifications = request.POST.get("specifications")

        laptop = Laptop.objects.create(
            student_id=student,
            serial_number=serial_number,
            make=make,
            model=model,
            color=color,
            specifications=specifications,
        )

    return render(request, "laptops/new_laptop.html")


@login_required(login_url="/users/login/")
def students(request):
    students = Student.objects.all()

    paginator = Paginator(students, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, "students": students}

    return render(request, "students/students.html", context)


@login_required(login_url="/users/login/")
def new_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        registration_number = request.POST.get("reg_number")
        id_number = request.POST.get("id_number")
        course = request.POST.get("course")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        gender = request.POST.get("gender")

    return render(request, "students/new_student.html")


@login_required(login_url="/users/login/")
def laptop_movements(request):
    laptop_movements = LaptopMovement.objects.all().order_by("-created")

    paginator = Paginator(laptop_movements, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}
    return render(request, "checkins/checkins.html", context)


@login_required(login_url="/users/login/")
def new_laptop_movement(request):
    if request.method == "POST":
        laptop = request.POST.get("laptop")
        student = request.POST.get("students")
        movement_type = request.POST.get("movement_type")

        LaptopMovement.objects.create(
            laptop_id=laptop, student_id=student, movement_type=movement_type
        )
    return render(request, "checkins/new_checkin.html")
