from django import forms  
from.models import *
from django.contrib.auth.models import User  
#from Admin.models import Designations,Salary


class ContactForm(forms.Form):		
	name=forms.CharField(required=True)
	email=forms.CharField(required=True)
	phone_number=forms.CharField(required=True)
	message=forms.CharField()



class File_Upload(forms.ModelForm):  
    class Meta:  
        model = Drive  
        fields = ['file_name','file']  	


