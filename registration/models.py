from django.db import models

# Create your models here.
    
class Student(models.Model):
    name = models.CharField(max_length = 100)
    student_id = models.CharField(max_length = 20, unique =True)
    grade = models.CharField(max_length = 10)
    contact_info = models.CharField(max_length = 100)
    
    def __str__(self): 
        return self.name
    
class Laptop(models.Model):
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
    
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE) 
    date = models.DateField(auto_now_add = True)
    movement_type = models.CharField(max_length = 20, choices = MOVEMENT_CHOICES)
    
    def __str__(self):
        return f"{self.laptop} {self.movement_type} by {self.student} on {self.date}"
    
    
