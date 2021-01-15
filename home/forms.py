from django import forms  
from.models import *
from django.contrib.auth.models import User  


class ContactForm(forms.Form):		
	name=forms.CharField(required=True)
	email=forms.CharField(required=True)
	phone_number=forms.CharField(required=True)
	message=forms.CharField()
