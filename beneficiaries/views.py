from django.http import JsonResponse
from beneficiaries.models import BeneficiaryInformation
from beneficiaries.serializers import BeneficiaryInformationSerializer
from rest_framework.decorators import api_view


@api_view(['POST'])
def store(request):
    
    de_serializers = BeneficiaryInformationSerializer(data = request.data)
    
    if de_serializers.is_valid():
        de_serializers.save()
        return JsonResponse(de_serializers.data, safe=False)
    return JsonResponse("is not valid", safe=False)


@api_view(['PUT'])
def update(request, pk):    
    employee_information = BeneficiaryInformation.objects.get(pk=pk)
    de_serializers = BeneficiaryInformationSerializer(employee_information, data = request.data)
    if de_serializers.is_valid():
        de_serializers.save()
        return JsonResponse(de_serializers.data)
    
    
@api_view(['DELETE'])
def delete(request, pk):
    employee_information = BeneficiaryInformation.objects.get(pk=pk)
    employee_information.delete()
    
    return JsonResponse("done", safe=False)
    