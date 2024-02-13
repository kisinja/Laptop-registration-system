from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100) 
    address = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name 
    
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
    
class LaptopRegistration(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete = models.CASCADE)
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    registration_date = models.DateField(auto_now_add = True)
    
    STATUS_CHOICES = [
        ('active', 'Active'), 
        ('stolen', 'Stolen'),
        ('recovered', 'Recovered'), 
    ] 
    
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'active')
    
class TheftReport(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete = models.CASCADE)
    report_date = models.DateField(auto_now_add = True)
    details = models.TextField()
    
    STATUS_CHOICES = [
        ('unresolved', 'Unresolved'), 
        ('resolved', 'Resolved'),
    ] 
    
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES)
    
    
