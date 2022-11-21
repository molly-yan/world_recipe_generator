from django.db import models

# Create your models here.
class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True, blank=True)
    EmployeeName = models.CharField(max_length=100, blank=True)
    EmployeeFood = models.CharField(max_length=100, blank=True)
    EmployeeFoodUrl = models.CharField(max_length=100, blank=True)
