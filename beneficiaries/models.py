from django.db import models
from django_softdelete.models import SoftDeleteModel
from employees.models import EmployeeInformation

class BeneficiaryInformation(SoftDeleteModel):
    men = 'men'
    woman = 'woman'
    CHOICES = (
        (men, men),
        (woman, woman),
    )
    
    employeeInformation = models.ForeignKey(EmployeeInformation, on_delete=models.CASCADE, related_name='beneficiary_information')
    fullname = models.CharField(max_length=100)
    kinship = models.CharField(max_length=100)
    date_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=100)
    
        
    class Meta:
        db_table = 'beneficiary_informations'
