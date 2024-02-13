from django.contrib import admin
from .models import Student, Laptop,LaptopMovement

# Register your models here.

admin.site.register(Student)
admin.site.register(Laptop)
admin.site.register(LaptopMovement)
