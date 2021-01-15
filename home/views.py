from django.shortcuts import render, redirect  
from django.http import HttpResponse,HttpResponseRedirect  
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from pms import settings  
from .forms import * 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import generic
from django.views.generic import TemplateView, ListView

  



def home(request):
    return render(request,'home/home.html')


def about(request):
    return render(request,'home/about.html')

def search(request):
    return render(request,'home/search.html')


# def services(request):
#     return render(request,'home/services.html')    



def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    
    else:       
        form = ContactForm(request.POST)
        if form.is_valid():
            name =form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail('subject',
            name+'is trying to contact you.\nDetails are: \n'+'\nName: '+name+' \nContact Number: '+
                    phone_number+'\nEmail: '+email+'\nMessage from sender: \n'+message,
                    settings.EMAIL_HOST_USER,
                    ['ishwarmandloi25@gmail.com','digitalspiritmakeiteasy@gmail.com','hr@makeiteasy.org.in',],
                    fail_silently=False)
                messages.success(request,"Message Sent Successfully")
            except BadHeaderError:
                return HttpResponse('Invalid header found')                
            return redirect('contact')     

    return render(request, "home/contact.html", {'form': form})




def digital_pms(request):
    if request.method == "POST":
        contact_name  = request.POST.get('contact_name') 
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        obj=contact_details(contact_name=contact_name,phone_number=phone_number,email=email)
        obj.save()
        messages.success(request," Contact Successfully")
    return redirect('home')     


 




