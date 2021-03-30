from django.db import models
from django.contrib.auth.models import User
from time import sleep
import datetime
from datetime import datetime



###################################################################################################################################################################

RelationType=(

    ('Father','Father'),
    ('Mother','Mother'),
    ('Wife','Wife'),
    ('Children','Children'),
)


position=(

    ('Beginner','Beginner'),
    ('Intermediate','Intermediate'),
    ('Expert','Expert'),
)

###################################################################################################################################################################

gender=(
    ('Male','Male'),
    ('Female','Female'),
)



###################################################################################################################################################################



STATUS=((0,'Deactive'),(1,'Active'))
# POLICY_TYPES=(
# (0,"jan_dhan_yojna"),
# (1,"jivan_bima"),
# (2,"jivan_laabh"),

#)


###################################################################################################################################################################


PAY_FOR=(
("Annually","Annually"),
("Quarterly","Quarterly"),
("Monthly","Monthly"),
("HalfYear","HalfYear"),
("OneTime","OneTime")

)


###################################################################################################################################################################



STATE=(
("Andhra Pradesh","Andhra Pradesh"),
("Arunachal Pradesh","Arunachal Pradesh"),
("Assam","Assam"),
("Bihar","Bihar"),
("Chhattisgarh","Chhattisgarh"),
("Goa","Goa"),
("Gujarat","Gujarat"),
("Haryana","Haryana"),
("Himachal Pradesh","Himachal Pradesh"),
("Jharkhand","Jharkhand"),
("Karnataka","Karnataka"),
("Kerala","Kerala"),
("Madhya Pradesh","Madhya Pradesh"),
("Maharashtra","Maharashtra"),
("Manipur","Manipur"),
("Meghalaya","Meghalaya"),
("Mizoram","Mizoram"),
("Nagaland","Nagaland"),
("Odisha","Odisha"),
("Punjab","Punjab"),
("Rajasthan","Rajasthan"),
("Sikkim","Sikkim"),
("Tamil Nadu","Tamil Nadu"),
("Telangana","Telangana"),
("Tripura","Tripura"),
("Uttar Pradesh","Uttar Pradesh"),
("Uttarakhand","Uttarakhand"),
("West Bengal","West Bengal"),

)

###################################################################################################################################################################




COMPANY_NAME=(
("APOLLO MUNICH GIC LTD","APOLLO MUNICH GIC LTD"),
("Bajaj","Bajaj"),
("BAJAJ ALLINZ GIC LTD","BAJAJ ALLINZ GIC LTD"),
("BHARTI AXA GIC LTD","BHARTI AXA GIC LTD"),
("FUTURE GENERALLY GIC LTD","FUTURE GENERALLY GIC LTD"),
("GO-DIGIT GIC LTD","GO-DIGIT GIC LTD"),
("hdfc bank","hdfc bank"),
("HDFC ERGO GIC LTD","HDFC ERGO GIC LTD"),
("HDFC Life","HDFC Life"),
("ICICI LOMBARD GIC LTD","ICICI LOMBARD GIC LTD"),
("Iffco Tokio","Iffco Tokio"),
("IFFCO TOKIO GIC LTD","IFFCO TOKIO GIC LTD"),
("Kotak Life Insurance Company","Kotak Life Insurance Company"),
("LIBERTY INSURANCE CO LTD","LIBERTY INSURANCE CO LTD"),
("LIC","LIC"),
("LIC OF INDIA","LIC OF INDIA"),
("Life","Life"),
("Life insurance corporation of india","Life insurance corporation of india"),
("Max Bhupa","Max Bhupa"),
)


###################################################################################################################################################################


TAX_STATUS=(
("Yes","Yes"),
("No","No"),

)


###################################################################################################################################################################



MODE_OF_HOLDING=(
("Single","Single"),
("Family","Family"),

)


###################################################################################################################################################################


LEAD=(
("News_Paper","News_Paper"),
("Magazine","Magazine"),
("Advertising","Advertising"),
("Google","Google"),
("Gmail","Gmail"),
("Friends_Reference","Friends_Reference")

)


###################################################################################################################################################################



class PolicyType(models.Model):
    policy_type = models.CharField(max_length=50,unique=True)
    added_on =models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.policy_type


###################################################################################################################################################################


class Lic(models.Model):    
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email= models.EmailField(max_length=50)
    dob=models.CharField(max_length=50)
    contact=models.IntegerField()
    address_line_one=models.CharField(max_length=100)
    address_line_two=models.CharField(max_length=100)
    lendmark=models.CharField(max_length=100,default=None)
    city=models.CharField(max_length=100)
    state=models.CharField(choices=STATE,null=False,max_length=50)
    policy_type=models.ForeignKey('PolicyType',on_delete=models.CASCADE,related_name='PolicyType')
    policy_number=models.CharField(unique=True,null=False,max_length=10)
    premium=models.IntegerField()
    sum_assured=models.IntegerField()
    year_of_policy=models.IntegerField()
    pay_for=models.CharField(choices=PAY_FOR,null=False,max_length=50)
    beneficiary_name=models.CharField(max_length=50)
    created_on=models.CharField(max_length=50)
    last_payment_date=models.CharField(max_length=50)
    renew_date=models.CharField(max_length=20)
    status=models.IntegerField(choices=STATUS,default=1)
    commission=models.IntegerField()
    commission_date=models.CharField(max_length=50)

    # family_name = models.CharField(max_length=100,default=True,blank=True,null=True)
    # family_dob = models.CharField(max_length=100,blank=True,null=True)
    # relation_type = models.CharField(max_length=100,choices=RelationType,null=True)
    # gender = models.CharField(max_length=100, choices=gender,null=True)
    

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name
    

###################################################################################################################################################################

       
class Drive(models.Model):
    file_name = models.CharField(max_length=20)
    file = models.FileField()
    added_on =models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    


    def __str__(self):
        return self.file_name


###################################################################################################################################################################

   

class Lead(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    contact_no= models.IntegerField()
    companay_name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    area=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(choices=STATE,null=False,max_length=50)
    inquiry_date=models.CharField(max_length=20)
    inquiry_time=models.TimeField(auto_now_add=True)
    lead_source=models.CharField(choices=LEAD,null=False,max_length=50)
    lead_allocated_to=models.CharField(max_length=30)
    status=models.IntegerField(choices=STATUS,default=1)
    follow_up_date=models.CharField(max_length=20)
    follow_up_time=models.TimeField(auto_now_add=True)
    message=models.CharField(max_length=1000)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.full_name


###################################################################################################################################################################



class Discuss(models.Model):
    msg = models.CharField(max_length=1000)
    added_on = models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey(Lead, on_delete=models.CASCADE)    
    

    def __str__(self):
        return self.msg   
       

###################################################################################################################################################################


class Mutual_Fund(models.Model):
    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)
    dob        = models.CharField(max_length=30)
    email      = models.EmailField(max_length=30)
    contact_no = models.CharField(max_length=30) 
    address_line_one = models.CharField(max_length=30)
    address_line_two = models.CharField(max_length=30)
    lendmark= models.CharField(max_length=100,default=None)
    city= models.CharField(max_length=100)
    state= models.CharField(choices=STATE,null=False,max_length=50)
    statement_date = models.CharField(max_length=30)
    folio_no=models.CharField(unique=True,null=False,max_length=20)
    company_name= models.CharField(choices=COMPANY_NAME,null=False,max_length=50)
    premium=models.IntegerField()
    created_on=models.CharField(max_length=50)
    pay_for=models.CharField(choices=PAY_FOR,null=False,max_length=50)
    renew_date=models.CharField(max_length=20)
    bank_name = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=50)
    account_no = models.CharField(max_length=30)
    name_holder = models.CharField(max_length=30)
    tax_status = models.CharField(choices=TAX_STATUS,null=False,max_length=50)
    mode_of_holding= models.CharField(choices=MODE_OF_HOLDING,null=False,max_length=50)
    commission=models.IntegerField()
    commission_date=models.CharField(max_length=50)
    status=models.IntegerField(choices=STATUS,default=1)

    # family_name = models.CharField(max_length=100,blank=True,null=True)
    # family_dob = models.CharField(max_length=100,blank=True,null=True)
    # relation_type = models.CharField(max_length=100,blank=True,null=True)
    # gender = models.CharField(max_length=100, choices=gender,null=True)
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name   
    


###################################################################################################################################################################    