import json
import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from employees.serializers import EmployeeInformationSerializer

from .models import EmployeeInformation

@api_view(['GET'])
def index(self):
    employee_informations = EmployeeInformation.objects.all()
    serializers = EmployeeInformationSerializer(employee_informations, many=True)
    return JsonResponse(serializers.data, safe=False)

@api_view(['POST'])
def store(request):
    de_serializers = EmployeeInformationSerializer(data = request.data)
    if de_serializers.is_valid():
        de_serializers.save()
        return JsonResponse(de_serializers.data)
    
@api_view(['PUT'])
def update(request, pk):    
    employee_information = EmployeeInformation.objects.get(pk=pk)
    de_serializers = EmployeeInformationSerializer(employee_information, data = request.data)
    if de_serializers.is_valid():
        de_serializers.save()
        return JsonResponse(de_serializers.data)
    
    
@api_view(['DELETE'])
def delete(request, pk):
    employee_information = EmployeeInformation.objects.get(pk=pk)
    employee_information.delete()
    
    return JsonResponse("done", safe=False)
    