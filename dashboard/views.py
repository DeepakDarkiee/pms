from django.shortcuts import render, redirect  
from django.http import HttpResponse,HttpResponseRedirect  
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from pms import settings  
from django.utils.decorators import method_decorator
import csv
from django.core.paginator import Paginator
from .models import Lic,PolicyType
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from dashboard.models import Lic,Drive
from django.contrib.auth.models import User
from datetime import datetime, timedelta,date
from django.contrib import messages
from datetime import datetime, timedelta
from django.conf import settings
from account.models import register_table
from pms.settings import MAIL
from django.utils import timezone
# from reportlab.pdfgen import canvas  
from django.http import HttpResponse  
from django.http import FileResponse
#from pms.settings import register_pms
# import xlwt 
from dashboard.functions import handle_uploaded_file  
from .resources import LicResource
from tablib import Dataset
from .forms import File_Upload 

@login_required
def index(request):
    user = User.objects.get(username = request.user)
    lics = Lic.objects.filter(user__pk=user.id)
    userMail=request.user.get_username()
    # duesInTwoDays= Lic.objects.filter(user__pk=user.id,renew_date__range=[datetime.now().date(),datetime.now().date()+timedelta(days=2)],status=1).order_by('renew_date')
    duesInWeek= Lic.objects.filter(user__pk=user.id,renew_date__range=[datetime.now().date(),datetime.now().date()+timedelta(days=5)],status=1).order_by('renew_date')
    Overdues= Lic.objects.filter(user__pk=user.id,renew_date__lt=datetime.now().date(),status=1).order_by('renew_date')
    overDueCount= Overdues.count()
    current_date=date.today()
    Due_in_days={}
    for obj in duesInWeek:
    
        Due_in_days[obj.id]=datetime.strptime(obj.renew_date,'%Y-%m-%d').day-current_date.day
    return render(request,'dashboard/index.html',{
        # 'towDaysDues':duesInTwoDays,
        'weekDues':duesInWeek,
        'Due_in_days':Due_in_days,
        'overDueCount':overDueCount
        })



@login_required
def performance(request):
    return render(request,"dashboard/performance.html")




@login_required
def add_record(request):
    if request.method == "POST":
        user = User.objects.get(username = request.user)
        first_name  = request.POST.get('first_name') 
        middle_name  = request.POST.get('middle_name') 
        last_name  = request.POST.get('last_name')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        contact =request.POST.get('contact')
        address_line_one = request.POST.get('address_line_one')
        address_line_two = request.POST.get('address_line_two')
        lendmark= request.POST.get('lendmark')
        city= request.POST.get('city')
        state= request.POST.get('state')
        policy_number=request.POST.get('policy_number')
        premium= request.POST.get('premium')
        sum_assured= request.POST.get('sum_assured')
        year_of_policy = request.POST.get('year_of_policy')
        pay_for = request.POST.get('pay_for')
        beneficiary_name =request.POST.get('beneficiary_name')
        created_on =request.POST.get('created_on')
        renew_date=request.POST.get('renew_date')
        policy_type=PolicyType.objects.get(policy_type=request.POST.get('type'))
        #status=request.POST.get('status')
        obj=Lic(email=email,first_name=first_name,last_name=last_name,middle_name=middle_name, address_line_one=address_line_one,address_line_two=address_line_two,lendmark=lendmark,city=city,state=state,
        dob=dob,contact=contact,policy_number=policy_number,
        premium=premium,sum_assured=sum_assured,year_of_policy=year_of_policy,pay_for=pay_for,beneficiary_name=beneficiary_name,
        created_on=created_on,renew_date=renew_date,policy_type=policy_type,user = user)
        obj.save()
        #register_pms(email) 
        messages.success(request, ' Successfully Saved ')
        return redirect("/show_record")                 
    policy_type=PolicyType.objects.all()
    return render(request,'dashboard/add_record.html',{'context':policy_type}) 
            


    
    
@login_required
def show_record(request):
    user = User.objects.get(username = request.user)   
    lics = Lic.objects.filter(user__pk=user.id)
    paginator=Paginator(lics,6)
    page_number= request.GET.get('page')
    page_obj =paginator.get_page(page_number)
    return render(request,'dashboard/show_record.html',{'page_obj':page_obj})   


@login_required
def edit_policy(request, id):  
    lics = Lic.objects.get(id=id) 
    policy_type=PolicyType.objects.all()
    return render(request,'dashboard/edit_policy.html', {'lics':lics,'context':policy_type})      


@login_required
def view_policy(request, id):  
    lics = Lic.objects.get(id=id) 
    return render(request,'dashboard/view_policy.html', {'lics':lics})      


@login_required
def add_policy(request):
    if request.method == "POST":
        user = User.objects.get(username = request.user)
        policy_type  = request.POST.get('policy_type')
        obj=PolicyType(policy_type=policy_type,user=user)
        obj.save()
        messages.success(request, 'Successfully Saved ')
        return HttpResponseRedirect('/add_record')

    return render(request,"dashboard/add_policy.html")



@login_required
def update_policy(request, id):  
    lics = Lic.objects.get(id=id)  
    if request.method == "POST":
        user = User.objects.get(username = request.user)
        lics.first_name  = request.POST.get('first_name','') 
        lics.last_name  = request.POST.get('last_name','')
        lics.email = request.POST.get('email','')
        lics.dob = request.POST.get('dob','')
        lics.contact =request.POST.get('contact','')
        lics.address_line_one = request.POST.get('address_line_one','')
        lics.address_line_two = request.POST.get('address_line_two','')
        lics.city=request.POST.get('city','')
        lics.state=request.POST.get('state','')
        lics.policy_number=request.POST.get('policy_number','')
        lics.premium= request.POST.get('premium','')
        lics.pay_for = request.POST.get('pay_for','')
        lics.sum_assured= request.POST.get('sum_assured','')
        lics.year_of_policy = request.POST.get('year_of_policy','')
        lics.beneficiary_name =request.POST.get('beneficiary_name','')
        lics.renew_date=request.POST.get('renew_date','')
        # lics.policy_type=request.POST.get('type','')
        lics.policy_type=PolicyType.objects.get(policy_type=request.POST.get('type',''))
        lics.status=request.POST.get('status','')
        lics.save()
        messages.success(request, ' Successfully Updated ')
    return redirect('/show_record')

def updateRenewDate(request):
    pno=request.POST['PolicyNo']
    print(pno)
    lics = Lic.objects.get(policy_number=pno)
    if request.method == "POST":
        lics.renew_date  = request.POST.get('RenewDate','')
        lics.save()
        messages.success(request, ' Successfully Paid ')
        return redirect('/index')

def updateRenewDateOverDue(request):
    print(request.POST)
    pno=request.POST['PolicyNo']
    lics = Lic.objects.get(policy_number=pno)
    if request.method == "POST":
        lics.renew_date  = request.POST.get('RenewDate','')
        lics.save()
        messages.success(request, ' Successfully Paid ')
        return redirect('/over_due')


def over_due(request):
    user = User.objects.get(username = request.user)
    lics = Lic.objects.filter(user__pk=user.id)
    userMail=request.user.get_username()
    # duesInTwoDays= Lic.objects.filter(user__pk=user.id,renew_date__range=[datetime.now().date(),datetime.now().date()+timedelta(days=2)],status=1).order_by('renew_date')
    duesInWeek= Lic.objects.filter(user__pk=user.id,renew_date__lt=datetime.now().date(),status=1).order_by('renew_date')
    overDueCount= duesInWeek.count()
    # todays date
    current_date=date.today()
    Due_in_days={}
    for obj in duesInWeek:
        Due_in_days[obj.id]=datetime.strptime(obj.renew_date,'%Y-%m-%d').day-current_date.day
    return render(request,'dashboard/over_due.html',{'weekDues':duesInWeek,
        'Due_in_days':Due_in_days,})


    

@login_required
def delete_policy(request, id):  
    lics = Lic.objects.get(id=id)  
    lics.delete() 
    messages.success(request, 'Successfully Deleted')
    return redirect('/show_record')     




class SearchResultsView(ListView):
    model = Lic
    template_name = 'dashboard/search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q') # new
        object_list = Lic.objects.filter(
            Q(first_name__icontains=query) | Q(policy_number__icontains=query)
        )
        return object_list



class SearchView(ListView):
    model = Drive
    template_name = 'dashboard/search_file.html'
    
    def get_queryset(self):
        query = self.request.GET.get('qr') # new
        objects_list = Drive.objects.filter(
            Q(file='query')
        )
        print(objects_list)
        return objects_list





def sort_record(request):
    user = User.objects.get(username = request.user)
    sorting = request.GET.get('sorting')
    lics = Lic.objects.filter(user__pk=user.id) 
    print(sorting)
    if sorting =='status':
        lics = Lic.objects.filter(user__pk=user.id,status=1).order_by('renew_date')
        return render(request,'dashboard/show_record.html',{
            'page_obj':lics,
            })  
    else:
        lics = Lic.objects.filter(user__pk=user.id).order_by('-'+sorting)
        return render(request,'dashboard/show_record.html',{
            'page_obj':lics,
            })  


def export_data(request):
    user = User.objects.get(username = request.user)
    if request.method == 'POST':
        file_format = request.POST['file-format']
        lic_resource = LicResource()
        queryset = Lic.objects.filter(user__pk=user.id)
        dataset = lic_resource.export(queryset)
        
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="PmsData_Backup.csv"'
            return response        
        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="PmsData_Backup.json"'
            return response

        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="PmsData_Backup.xls"'
            return response   
          
    
    return redirect('/show_record')



def import_data(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        lic_resource = LicResource()
        dataset = Dataset()
        new_lics = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_lics.read().decode('utf-8'),format='csv')
            result = lic_resource.import_data(dataset, dry_run=True)        
        
        elif file_format == 'JSON':
            imported_data = dataset.load(new_lics.read().decode('utf-8'),format='json')
            result = lic_resource.import_data(dataset, dry_run=True)  

        elif file_format == 'XLS (Excel)':
            
            imported_data = dataset.load(new_lics.read())
            result = lic_resource.import_data(dataset, dry_run=True)  

            
        if not result.has_errors():
            lic_resource.import_data(dataset, dry_run=False)

    return redirect('/show_record')   
 

 

def my_drive(request):    
    if request.method == 'POST': 
        user = User.objects.get(username = request.user)
        print(user)
        drive = File_Upload(request.POST, request.FILES) 
        print(drive) 
        if drive.is_valid():  
            handle_uploaded_file(request.FILES['file'])
            obj=drive.save(commit=False)   
            obj.user = request.user
            obj.save()
            return redirect('/my-drive')   
    else:  
        drive = File_Upload()  
        user = User.objects.get(username = request.user)
        objs = Drive.objects.filter(user__pk=user.id) 
        return render(request,"dashboard/my_drive.html",{'form':drive,'objs':objs}) 



@login_required
def delete_drive(request, id):
    objs = Drive.objects.get(id=id)
    objs.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect('/my-drive')     


@login_required
def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application/adminupload")
            response['content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
