# base counter for total policy
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

def counter(request):
    # from django.contrib.auth.decorators import login_required
    from dashboard.models import Lic,Drive
    from account.models import register_table
    from django.contrib.auth.models import User
    from datetime import datetime, timedelta
    
    # @login_required
    if(request.user.id):
        # today=datetime.date.today()
        # print(today)
        
        context = {}
        data = register_table.objects.get(user__id=request.user.id)
        context["data"] = data

        
        user = User.objects.get(username = request.user)
        lics = Lic.objects.filter(user__pk=user.id)
        dues= Lic.objects.filter(user__pk=user.id,renew_date__range=[datetime.now().date(),datetime.now().date()+timedelta(days=7)],status=1).count()
        # dues= Lic.objects.filter(user__pk=user.id,renew_date__in=timedelta(days=7),status=1).count()
        active = Lic.objects.filter(user__pk=user.id,status=1).count()
        drive = Drive.objects.filter(user__pk=user.id).count()
        print(drive)
        count = lics.count()
        return {
        'count':count,
        'active':active,
        'dues':dues,
        'data': data,
        'drive':drive,
        }
    return {}



import asyncio
from pms.settings import MAIL
from dashboard.models import Lic,Drive
from django.contrib.auth.models import User
from datetime import datetime, timedelta



async def main():
    reminder7day= Lic.objects.filter(renew_date=datetime.now().date()+timedelta(days=7),status=1)     
    for i in reminder7day:
        if datetime.now().hour is 15:
            print(i.email)
            MAIL(i.email)
    reminder2day= Lic.objects.filter(renew_date=datetime.now().date()+timedelta(days=2),status=1)     
    for i in reminder2day:
        
            MAIL(i.email)

asyncio.run(main())
    
