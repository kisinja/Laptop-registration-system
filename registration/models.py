from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)
    
class Student(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    name = models.CharField(max_length = 255)
    registration_number = models.CharField(max_length=255, null=True)
    id_number = models.CharField(max_length=255, null=True)
    course = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, null=True)
    
    def __str__(self): 
        return self.name
    
class Laptop(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    serial_number = models.CharField(max_length = 100)
    make = models.CharField(max_length = 50)
    model = models.CharField(max_length = 50)
    color = models.CharField(max_length = 20)
    specifications = models.TextField() 
    
    def __str__(self):
        return f"{self.make} {self.model} ({self.serial_number})"
    
class LaptopMovement(models.Model):
    
    MOVEMENT_CHOICES = [
        ('Check Out', 'Check Out'),
        ('Check In', 'Check In'), 
    ]
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE) 
    movement_type = models.CharField(max_length = 20, choices = MOVEMENT_CHOICES)
    
    def __str__(self):
        return f"{self.laptop} {self.movement_type} by {self.student} on {self.date}"
    
    
