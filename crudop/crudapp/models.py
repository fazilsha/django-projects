from django.db import models

# Create your models here.
class Designation(models.Model):
    designation = models.CharField(max_length=30)
    def __str__(self):
        return self.designation
class Employee(models.Model):
    name = models.CharField(max_length=30)
    emp_id = models.CharField(max_length=30)
    mobileno = models.CharField(max_length=30)
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE)
