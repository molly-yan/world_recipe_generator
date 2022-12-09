from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from NewApp.models import Employees
from NewApp.serializers import EmployeeSerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def employeeApi(request,id=0,email=""):
    #if request.method=='GET':
        #employees = Employees.objects.all()
        #employees_serializer = EmployeeSerializer(employees, many=True)
        #return JsonResponse(employees_serializer.data, safe=False)

    ##------------------------GET------------------------##
    #   returns all data from User table in Json Format
    ##---------------------------------------------------##
    if request.method=='GET'and id==0:
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
      
    ##------------------------GET SELECT------------------------##
    #   returns data from user with the given ID
    ##----------------------------------------------------------##
    elif request.method=='GET'and id!=0:   
        employee=Employees.objects.get(EmployeeId=id)
        employee_serializer = EmployeeSerializer(employee)
        return JsonResponse(employee_serializer.data, safe = False)

    elif request.method=='GET' and email!="":
        employee=Employees.objects.get(EmployeeEmial=email)
        employee_serializer = EmployeeSerializer(employee)
        return JsonResponse(employee_serializer.data, safe = False)

    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        employee_data = JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer=EmployeeSerializer(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)
"""
@csrf_exempt
def foodPicApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
"""


@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)