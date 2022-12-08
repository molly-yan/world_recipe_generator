from django.db import models

# Create your models here.
class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True, blank=True)
    EmployeeName = models.CharField(max_length=100, blank=True)
    EmployeeEmail = models.CharField(max_length=100, blank=True)
    EmployeeCountry = models.CharField(max_length=100, blank=True)
    EmployeeCuisine = models.CharField(max_length=100, blank=True)
    EmployeeCuisineCountry = models.CharField(max_length=100, blank=True)

