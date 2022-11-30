from beneficiaries.models import BeneficiaryInformation
from rest_framework import serializers


class BeneficiaryInformationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BeneficiaryInformation
        fields= ('__all__')
         
        def create(self, validated_data):
            return BeneficiaryInformation.objects.create(**validated_data)
        
        def update(self, instance, validated_data):
            instance.update(**validated_data)
            return instance

   