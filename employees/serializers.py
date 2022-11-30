from beneficiaries.serializers import BeneficiaryInformationSerializer
from employees.models import EmployeeInformation
from rest_framework import serializers


class EmployeeInformationSerializer(serializers.ModelSerializer):
    beneficiary_information = BeneficiaryInformationSerializer(many=True, read_only=True)
    class Meta:
        model = EmployeeInformation
        fields= ('__all__')
         
        def create(self, validated_data):
            return EmployeeInformation.objects.create(**validated_data)
        
        def update(self, instance, validated_data):
            instance.update(**validated_data)
            return instance

   