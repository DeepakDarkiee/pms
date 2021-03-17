# base counter for total policy
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()


###################################################################################################################################################################



def counter(request):
    # from django.contrib.auth.decorators import login_required
    from dashboard.models import Lic,Drive,Mutual_Fund
    from account.models import register_table
    from django.contrib.auth.models import User
    from datetime import datetime, timedelta
    from datetime import date 
    
    # @login_required
    if(request.user.id):
        
        
        
        # context = {}
        # data = register_table.objects.get(user__id=request.user.id)
        # context["data"] = data

        todays_date = date.today() 
        user = User.objects.get(username = request.user)
      
        lics = Lic.objects.filter(user__pk=user.id)
        dues= Lic.objects.filter(user__pk=user.id,renew_date__range=[datetime.now().date(),datetime.now().date()+timedelta(days=7)],status=1).count()
        active = Lic.objects.filter(user__pk=user.id,status=1).count()
        count = lics.count()


        # get_policy= Lic.objects.filter(created_on__year=request.POST['year'],created_on__month=request.POST['month'])
        # print(get_policy)
        # count = get_policy.count()

        
            

        # commissions = Lic.objects.filter(user__pk=user.id)
        # if commissions.exists():
        #     commission_list =list()
        #     for commission in commissions:
        #         com=commission.commission
        #         commission_list.append(com)
        #     total_com=sum(commission_list)
        # else:
        #     total_com=0

                
        
        funds = Mutual_Fund.objects.filter(user__pk=user.id)
        fund_dues = Mutual_Fund.objects.filter(user__pk=user.id,renew_date__range=[datetime.now().date(),datetime.now().date()+timedelta(days=7)],status=1).count()
        active_fund = Mutual_Fund.objects.filter(user__pk=user.id,status=1).count()
        count_fund = funds.count()
        

        # fund_commission = Mutual_Fund.objects.filter(user__pk=user.id)
        # if fund_commission.exists():
        #     commission_list = list()
        #     for commission in fund_commission:
        #         com =commission.commission
        #         commission_list.append(com)
        #     total_fund_com = sum(commission_list)
        # else:
        #     total_fund_com=0

        # overall_commission = total_fund_com + total_com
                

        return {
        
        'fund_dues':fund_dues,
        'active_fund':active_fund,
        'count_fund':count_fund,
        'count':count,
        'active':active,
        'dues':dues,
        #'total_com':total_com,
        #'total_fund_com':total_fund_com,
        #'overall_commission': overall_commission,
        'todays_date':todays_date,
        # 'get_policy':get_policy,
        #'data':data,
        
        }
    return {}



###################################################################################################################################################################




import asyncio
from pms.settings import MAIL
from dashboard.models import Lic,Drive
from django.contrib.auth.models import User
from datetime import datetime, timedelta



async def main():
   reminder5day= Lic.objects.filter(renew_date=datetime.now().date()+timedelta(days=5),status=1)
   for i in reminder5day:
       if datetime.now().hour is 15:
           print(i.email)
           MAIL(i.email)

asyncio.run(main())



###################################################################################################################################################################