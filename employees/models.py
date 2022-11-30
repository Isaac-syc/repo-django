from django.db import models
from django_softdelete.models import SoftDeleteModel


class EmployeeInformation(SoftDeleteModel):
      
    fullname = models.CharField(max_length=100, null=True, blank=True)
    photo_path = models.ImageField(blank='', default='',upload_to='img')
    job = models.CharField(max_length=40)
    salary = models.DecimalField(default=0, decimal_places=2, max_digits=20)
    status = models.CharField(max_length=50)
    hiring_date = models.DateField(blank=True, null=True)
    
    class Meta:
        db_table = 'employees_Informations'
    

    
    
