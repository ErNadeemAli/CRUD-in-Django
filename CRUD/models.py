from django.db import models

# Create your models here.
class Employee(models.Model):
    e_id=models.CharField(max_length=10,default='')
    e_name=models.CharField(max_length=50)
    e_email=models.EmailField(max_length=200)
    e_contact=models.CharField(max_length=15)
    e_address=models.CharField(max_length=255)
    class Meta:
        db_table = 'Employee_table'
        