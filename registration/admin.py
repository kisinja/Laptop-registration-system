from django.contrib import admin
from .models import School, Student, Laptop, LaptopRegistration, TheftReport

# Register your models here.

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Laptop)
admin.site.register(LaptopRegistration)
admin.site.register(TheftReport)  
