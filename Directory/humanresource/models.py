from django.db import models

# Create your models here.
class Department(models.Model):
    ID = models.AutoField(primary_key=True)  
    DepartmentName = models.CharField(max_length=50, null=False)  
    IsActive = models.BooleanField(max_length=1, null=False, default=True)  

    def __str__(self):
        return self.DepartmentName

class Staff(models.Model):
    FirstName = models.CharField(max_length=50, null=False)  
    MiddleName = models.CharField(max_length=50, null=True, blank=True)  
    LastName = models.CharField(max_length=50, null=False)  
    EmailID = models.EmailField(max_length=50, null=False)  
    ContactNo = models.CharField(max_length=10, null=False)  
    Department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)  

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"