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
from dashboard.models import Lic,Drive,Lead,Discuss,Mutual_Fund
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
from .resources import LicResource ,LeadResource,FundResource
from tablib import Dataset
from .forms import File_Upload,LeadForm 
from django.views.generic.edit import CreateView

#######################################################################################################


@login_required
def index(request):
    user = User.objects.get(username = request.user)
    lics = Lic.objects.filter(user__pk=user.id)
    userMail=request.user.get_username()

    duesInWeekPolicy= Lic.objects.filter(user__pk=user.id,renew_date__range=[datetime.now().date(),datetime.now().date()+timedelta(days=7)],status=1).order_by('renew_date')
    Overdues= Lic.objects.filter(user__pk=user.id,renew_date__lt=datetime.now().date(),status=1).order_by('renew_date')
    overDueCount= Overdues.count()    
    current_date=date.today()
    
    Due_in_days={}
    for obj in duesInWeekPolicy:
    
        Due_in_days[obj.id]=datetime.strptime(obj.renew_date,'%Y-%m-%d').day-current_date.day
    return render(request,'dashboard/index.html',{
    
        'duesInWeekPolicy':duesInWeekPolicy,
        'Due_in_days':Due_in_days,
        'overDueCount':overDueCount,

        })

    user = User.objects.get(username = request.user)
    funds = Mutual_Fund.objects.filter(user__pk=user.id)
    userMail=request.user.get_username()


    duesInWeekfund= Mutual_Fund.objects.filter(user__pk=user.id,renew_date__range=[datetime.now().date(),datetime.now().date()+timedelta(days=7)],status=1).order_by('renew_date')
    FundOverdues= Mutual_Fund.objects.filter(user__pk=user.id,renew_date__lt=datetime.now().date(),status=1).order_by('renew_date')
    fundoverDueCount= FundOverdues.count()    
    current_date=date.today()


    Due_in_days={}
    for obj in duesInWeekfund:
    
        Due_in_days[obj.id]=datetime.strptime(obj.renew_date,'%Y-%m-%d').day-current_date.day
    return render(request,'dashboard/index.html',{
    
        'duesInWeekfund':duesInWeekfund,
        'Due_in_days':Due_in_days,
        'fundoverDueCount':fundoverDueCount,

        })

########################################################################################################



@login_required
def commission(request):        
    return render(request,'dashboard/commission.html')




@login_required
def insurance(request):
    return HttpResponse("<marquee><h1>page under construction </h1></marquee")
    
    
@login_required
def govt_scheme(request):
    return HttpResponse("<marquee><h1>page under construction </h1></marquee")
    
    
@login_required
def premium_calculator(request):
    return HttpResponse("<marquee><h1>page under construction </h1></marquee")    
    





########################################################################################################

@login_required
def add_mutual_fund(request):
    if request.method == 'POST':
        user = User.objects.get(username = request.user)
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        dob = request.POST.get("dob")
        email = request.POST.get("email")
        contact_no = request.POST.get("contact_no")
        address_line_one = request.POST.get("address_line_one")
        address_line_two = request.POST.get("address_line_two")
        lendmark= request.POST.get('lendmark')
        city = request.POST.get('city')
        state = request.POST.get('state')
        statement_date= request.POST.get('statement_date')
        folio_no = request.POST.get('folio_no')
        company_name= request.POST.get('company_name')
        premium=request.POST.get('premium')
        created_on=request.POST.get('created_on')
        pay_for = request.POST.get('pay_for')
        renew_date=request.POST.get('renew_date')
        bank_name= request.POST.get('bank_name')
        ifsc_code=request.POST.get('ifsc_code')
        account_no=request.POST.get('account_no')
        name_holder= request.POST.get('name_holder')
        tax_status = request.POST.get('tax_status')
        mode_of_holding= request.POST.get('mode_of_holding')
        commission=request.POST.get('commission')
        commission_date=request.POST.get('commission_date')

        family_name = request.POST.get('family_name')
        family_dob = request.POST.get('family_dob')
        relation_type = request.POST.get('relation_type')
        gender = request.POST.get('gender') 

        obj=Mutual_Fund(first_name=first_name,last_name=last_name,dob=dob,email=email,contact_no=contact_no,
            address_line_one=address_line_one,pay_for=pay_for,created_on=created_on,address_line_two=address_line_two,lendmark=lendmark,city=city,
            state=state,statement_date=statement_date,premium=premium,folio_no=folio_no,company_name=company_name,name_holder=name_holder,
            tax_status=tax_status,commission=commission,commission_date=commission_date,renew_date=renew_date,account_no=account_no,ifsc_code=ifsc_code,mode_of_holding=mode_of_holding,bank_name=bank_name,
            family_name=family_name,family_dob=family_dob,relation_type=relation_type,gender=gender,user=user)
        obj.save()

        messages.success(request,'successfully Save')
        return redirect('/show-mutual-fund')

    return render(request,'dashboard/add_mutual_fund.html') 



@login_required
def show_mutual_fund(request):
    user = User.objects.get(username = request.user)   
    funds = Mutual_Fund.objects.filter(user__pk=user.id)
    paginator=Paginator(funds,6)
    page_number= request.GET.get('page')
    page_obj =paginator.get_page(page_number)
    return render(request,'dashboard/show_mutual_fund.html',{'page_obj':page_obj}) 


@login_required
def view_fund(request, id):  
    funds = Mutual_Fund.objects.get(id=id) 
    return render(request,'dashboard/view_fund.html', {'funds':funds})


@login_required
def edit_fund(request, id):  
    funds = Mutual_Fund.objects.get(id=id) 
    return render(request,'dashboard/edit_fund.html', {'funds':funds})


@login_required
def update_fund(request, id):  
    funds = Mutual_Fund.objects.get(id=id)  
    if request.method == "POST":
        user = User.objects.get(username = request.user)
        funds.first_name  = request.POST.get('first_name','') 
        funds.last_name  = request.POST.get('last_name','')
        funds.dob = request.POST.get('dob','')
        funds.email = request.POST.get('email','')
        funds.contact_no = request.POST.get('contact_no','')
        funds.address_line_one = request.POST.get('address_line_one','')
        funds.address_line_two = request.POST.get('address_line_two','')
        funds.lendmark = request.POST.get('lendmark','')
        funds.city = request.POST.get('city','')
        funds.state = request.POST.get('state','')
        funds.statement_date = request.POST.get('statement_date','')
        funds.folio_no =request.POST.get('folio_no','')
        funds.company_name = request.POST.get('company_name','')
        funds.bank_name = request.POST.get('bank_name','')
        funds.ifsc_code = request.POST.get('ifsc_code','')
        funds.account_no = request.POST.get('account_no','')
        funds.name_holder = request.POST.get('name_holder','')
        funds.tax_status = request.POST.get('tax_status','')
        funds.mode_of_holding = request.POST.get('mode_of_holding','')
        funds.commission=request.POST.get('commission','')
        funds.commission_date=request.POST.get('commission_date','')
        funds.status=request.POST.get('status','')
        funds.save()
        #print('inquiry_time')
        messages.success(request, ' Successfully Updated ')
    return redirect("/show-mutual-fund")


@login_required
def delete_fund(request,id):
    funds = Mutual_Fund.objects.get(id = id)
    funds.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect('/show-mutual-fund')



class SearchFundView(ListView):
    model = Mutual_Fund
    template_name = 'dashboard/search_fund.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q') # new
        object_list = Mutual_Fund.objects.filter(
            Q(first_name__icontains=query) | Q(folio_no__icontains=query)
        )
        return object_list



def fund_over_due(request):
    user = User.objects.get(username = request.user)
    funds = Mutual_Fund.objects.filter(user__pk=user.id)
    userMail=request.user.get_username()
    
    duesInWeek= Mutual_Fund.objects.filter(user__pk=user.id,renew_date__lt=datetime.now().date(),status=1).order_by('renew_date')
    overDuefund= duesInWeek.count()
    
    current_date=date.today()
    
    Due_in_days={}
    for obj in duesInWeek:
        Due_in_days[obj.id]=datetime.strptime(obj.renew_date,'%Y-%m-%d').day-current_date.day
    return render(request,'dashboard/fund_over_due.html',{'weekDues':duesInWeek,
        'Due_in_days':Due_in_days,})




def export_fund(request):
    user = User.objects.get(username = request.user)
    if request.method == 'POST':
        file_format = request.POST['file-format']
        fund_resource = FundResource()
        queryset = Mutual_Fund.objects.filter(user__pk=user.id)
        dataset = fund_resource.export(queryset)
        
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="fundData_Backup.csv"'
            return response        
        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="fundData_Backup.json"'
            return response

        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="fundData_Backup.xls"'
            return response   
          
    
    return redirect('/show-mutual-fund')


 

def import_fund(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        fund_resource = FundResource()
        dataset = Dataset()
        new_fund = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_fund.read().decode('utf-8'),format='csv')
            result = fund_resource.import_data(dataset, dry_run=True)        
        
        elif file_format == 'JSON':
            imported_data = dataset.load(new_fund.read().decode('utf-8'),format='json')
            result = fund_resource.import_data(dataset, dry_run=True)  

        elif file_format == 'XLS (Excel)':
            
            imported_data = dataset.load(new_fund.read())
            result = fund_resource.import_data(dataset, dry_run=True)  

            
        if not result.has_errors():
            fund_resource.import_data(dataset, dry_run=False)

    return redirect('/show-mutual-fund') 



#######################################################################################################################

@login_required
def add_lead(request):
    if request.method == "POST":
        user = User.objects.get(username = request.user)
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        companay_name = request.POST.get('companay_name')
        address =  request.POST.get('address')
        area = request.POST.get('area')
        city = request.POST.get('city')
        state = request.POST.get('state')
        inquiry_date = request.POST.get('inquiry_date')
        inquiry_time = request.POST.get('inquiry_time')
        lead_source = request.POST.get('lead_source')
        lead_allocated_to = request.POST.get('lead_allocated_to')
        follow_up_date = request.POST.get('follow_up_date')
        follow_up_time = request.POST.get('follow_up_time')
        message=request.POST.get('message')
        obj=Lead(full_name=full_name,email=email,contact_no=contact_no,companay_name=companay_name,area=area,state=state,lead_source=lead_source,inquiry_time=inquiry_time,city=city,address=address,
            lead_allocated_to=lead_allocated_to,message=message,follow_up_date=follow_up_date,inquiry_date=inquiry_date,follow_up_time=follow_up_time,user=user)
    
        obj.save()

        messages.success(request,"successfully Save")
        return redirect("/manage-lead")

    return render(request,"dashboard/lead.html")


@login_required
def manage_lead(request):
    user = User.objects.get(username = request.user)
    lead = Lead.objects.filter(user__pk=user.id)
    paginator=Paginator(lead,6)
    page_no= request.GET.get('page')
    page_object =paginator.get_page(page_no)
    return render(request,'dashboard/show_lead.html',{'page_object':page_object}) 



@login_required
def edit_lead(request,id):
    leads = Lead.objects.get(id=id)
    return render(request,'dashboard/edit_lead.html',{'leads':leads })


@login_required
def view_lead(request, id):  
    leads = Lead.objects.get(id=id) 
    return render(request,'dashboard/view_lead.html', {'leads':leads})      


@login_required
def edit_history(request,id):
    user = User.objects.get(username = request.user)
    leads = Lead.objects.get(id=id)
    discu = Discuss.objects.filter(reporter=id)
    return render(request,'dashboard/history.html',{'leads':leads,'discu':discu})

 
@login_required
def discussion(request):
    if request.method == "POST":
        reporter = Lead.objects.get(id=request.POST.get('id'))
        msg  = request.POST.get('msg')
        obj=Discuss(msg=msg,reporter=reporter)
        obj.save()
        messages.success(request, 'Successfully Saved ')
        return redirect('/manage-lead')

    return render(request,"dashboard/history.html")


@login_required
def update_lead(request, id):  
    leads = Lead.objects.get(id=id)  
    if request.method == "POST":
        user = User.objects.get(username = request.user)
        leads.full_name  = request.POST.get('full_name','') 
        leads.email  = request.POST.get('email','')
        leads.contact_no = request.POST.get('contact_no','')
        leads.companay_name = request.POST.get('companay_name','')
        leads.address = request.POST.get('address','')
        leads.area = request.POST.get('area','')
        leads.city = request.POST.get('city','')
        leads.state = request.POST.get('state','')
        leads.inquiry_date = request.POST.get('inquiry_date','')
        leads.inquiry_time = request.POST.get('inquiry_time')
        leads.lead_source = request.POST.get('lead_source','')
        leads.lead_allocated_to =request.POST.get('lead_allocated_to','')
        leads.status = request.POST.get('status','')
        leads.follow_up_date = request.POST.get('follow_up_date','')
        leads.follow_up_time = request.POST.get('follow_up_time','')
        #leads.message =request.POST.get('message','')
        leads.save()
        #print('inquiry_time')
        messages.success(request, ' Successfully Updated ')
    return redirect("/manage-lead")



@login_required
def update_history(request, id):  
    leads = Lead.objects.get(id=id)  
    if request.method == "POST":
        user = User.objects.get(username = request.user)
        leads.full_name  = request.POST.get('full_name','') 
        leads.follow_up_date = request.POST.get('follow_up_date','')
        leads.follow_up_time = request.POST.get('follow_up_time','')
        #leads.message =request.POST.get('message','')
        leads.save()
        #print('inquiry_time')
        messages.success(request, ' Successfully Updated ')
    return redirect("/manage-lead")



def export_lead(request):
    user = User.objects.get(username = request.user)
    if request.method == 'POST':
        file_format = request.POST['file-format']
        lead_resource = LeadResource()
        queryset = Lead.objects.filter(user__pk=user.id)
        dataset = lead_resource.export(queryset)
        
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="leadData_Backup.csv"'
            return response        
        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="leadData_Backup.json"'
            return response

        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="leadData_Backup.xls"'
            return response   
          
    
    return redirect('/manage-lead')


 

def import_lead(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        lead_resource = LeadResource()
        dataset = Dataset()
        new_lead = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_lead.read().decode('utf-8'),format='csv')
            result = lead_resource.import_data(dataset, dry_run=True)        
        
        elif file_format == 'JSON':
            imported_data = dataset.load(new_lead.read().decode('utf-8'),format='json')
            result = lead_resource.import_data(dataset, dry_run=True)  

        elif file_format == 'XLS (Excel)':
            
            imported_data = dataset.load(new_lead.read())
            result = lead_resource.import_data(dataset, dry_run=True)  

            
        if not result.has_errors():
            lead_resource.import_data(dataset, dry_run=False)

    return redirect('/manage-lead')  



@login_required
def delete_lead(request,id):
    leads = Lead.objects.get(id = id)
    leads.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect('/manage-lead')



class SearchLeadView(ListView):
    model = Lead
    template_name = 'dashboard/search_lead.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q') # new
        object_list = Lead.objects.filter(
            Q(full_name__icontains=query) 
        )
        return object_list




############################################################################################################################

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
        commission=request.POST.get('commission')
        commission_date=request.POST.get('commission_date')


        family_name = request.POST.getlist(('family_names[]'))
        print(family_name)
        family_name=','.join(family_name)

        family_dob = request.POST.getlist(('family_dob[]'))
        family_dob=','.join(family_dob)

        relation_type = request.POST.getlist(('relation_type[]'))
        relation_type=','.join(relation_type)

        gender = request.POST.getlist(('gender[]'))
        gender=','.join(gender)

        policy_type=PolicyType.objects.get(policy_type=request.POST.get('type'))
        last_payment_date=request.POST.get('last_payment_date')
        
        obj=Lic(email=email,first_name=first_name,last_name=last_name,middle_name=middle_name, address_line_one=address_line_one,address_line_two=address_line_two,lendmark=lendmark,city=city,state=state,
        dob=dob,contact=contact,policy_number=policy_number,family_name=family_name,family_dob=family_dob,relation_type=relation_type,gender=gender,
        premium=premium,sum_assured=sum_assured,year_of_policy=year_of_policy,pay_for=pay_for,beneficiary_name=beneficiary_name,
        created_on=created_on,commission=commission,commission_date=commission_date,renew_date=renew_date,policy_type=policy_type,last_payment_date=last_payment_date,user = user)
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
    
    family_name=list(lics.family_name.split(","))    
    family_dob=list(lics.family_dob.split(","))
    relation_type=list(lics.relation_type.split(","))
    gender=list(lics.gender.split(","))
    
    family_info=zip(family_name,family_dob,relation_type,gender)
    
    # family_info=zip([1,2,3],[4,5,6],[7,8,9],[10,11,12])
    return render(request,'dashboard/view_policy.html', {'lics':lics,'family':family_info})      





@login_required
def update_policy(request, id):  
    lics = Lic.objects.get(id=id)  
    if request.method == "POST":
        user = User.objects.get(username = request.user)
        lics.first_name  = request.POST.get('first_name','') 
        lics.middle_name  = request.POST.get('middle_name','')
        lics.last_name  = request.POST.get('last_name','')
        lics.email = request.POST.get('email','')
        lics.dob = request.POST.get('dob','')
        lics.contact =request.POST.get('contact','')        
        lics.address_line_one = request.POST.get('address_line_one','')
        lics.address_line_two = request.POST.get('address_line_two','')
        lics.lendmark=request.POST.get('lendmark','')
        lics.city=request.POST.get('city','')
        lics.state=request.POST.get('state','')
        lics.policy_number=request.POST.get('policy_number','')
        lics.premium= request.POST.get('premium','')
        lics.pay_for = request.POST.get('pay_for','')        
        lics.sum_assured= request.POST.get('sum_assured','')
        lics.year_of_policy = request.POST.get('year_of_policy','')
        lics.beneficiary_name =request.POST.get('beneficiary_name','')
        lics.created_on=request.POST.get('created_on','')
        lics.renew_date=request.POST.get('renew_date','')
        lics.commission=request.POST.get('commission','')
        lics.commission_date=request.POST.get('commission_date','')
        lics.last_payment_date=request.POST.get('last_payment_date','')
        lics.policy_type=PolicyType.objects.get(policy_type=request.POST.get('type',''))
        lics.status=request.POST.get('status','')

        lics.family_name = request.POST.getlist(('family_name[]'))
        lics.family_name=','.join(lics.family_name)

        lics.family_dob = request.POST.getlist(('family_dob[]'))
        lics.family_dob=','.join(lics.family_dob)

        lics.relation_type = request.POST.getlist(('relation_type[]'))
        lics.relation_type=','.join(lics.relation_type)

        lics.gender = request.POST.getlist(('gender[]'))
        lics.gender=','.join(lics.gender)

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
 




###################################################################################################################################


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




##################################################################################################################


@login_required
def performance(request):
    return render(request,"dashboard/performance.html")


######################################################################################################


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


###############################################################################################################