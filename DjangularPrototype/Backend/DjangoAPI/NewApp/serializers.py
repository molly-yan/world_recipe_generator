from rest_framework import serializers
from NewApp.models import Employees

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId',
                  'EmployeeName',
                  'EmployeeFood',
                  'EmployeeFoodUrl')