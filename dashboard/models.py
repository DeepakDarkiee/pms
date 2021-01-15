from django.db import models
from django.contrib.auth.models import User
from time import sleep
import datetime
from datetime import datetime


STATUS=((0,'Deactive'),(1,'Active'))
# POLICY_TYPES=(
# (0,"jan_dhan_yojna"),
# (1,"jivan_bima"),
# (2,"jivan_laabh"),

#     )

PAY_FOR=(
("Annually","Annually"),
("Quarterly","Quarterly"),
("Monthly","Monthly"),
("HalfYear","HalfYear"),

)


class PolicyType(models.Model):
    policy_type = models.CharField(max_length=50)
    added_on =models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.policy_type


class Lic(models.Model):    
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email= models.EmailField(max_length=50)
    dob=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    address_line_one=models.CharField(max_length=100)
    address_line_two=models.CharField(max_length=100)
    lendmark=models.CharField(max_length=100,default=None)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    policy_type=models.ForeignKey('PolicyType',on_delete=models.CASCADE,related_name='PolicyType')
    policy_number=models.CharField(unique=True,null=False,max_length=10)
    premium=models.IntegerField()
    sum_assured=models.IntegerField()
    year_of_policy=models.IntegerField()
    pay_for=models.CharField(choices=PAY_FOR,null=False,max_length=50)
    beneficiary_name=models.CharField(max_length=50)
    created_on=models.CharField(max_length=50)
    renew_date=models.CharField(max_length=20)
    status=models.IntegerField(choices=STATUS,default=1)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
    	return self.first_name

    

       
class Drive(models.Model):
    file_name = models.CharField(max_length=20)
    file = models.FileField()
    added_on =models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    


    def __str__(self):
        return self.file_name
   

   
       
