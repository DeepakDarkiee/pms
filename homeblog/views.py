from django.shortcuts import render, redirect  
from django.http import HttpResponse,HttpResponseRedirect  
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from pms import settings  
#from .forms import * 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import generic
from django.views.generic import TemplateView, ListView

  



def home(request):
    return render(request,'homeblog/index.html')


# def about(request):
#     return render(request,'home/about.html')

# def search(request):
#     return render(request,'home/search.html')
