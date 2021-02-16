from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Lic,PolicyType,Drive,Lead,Discuss,Mutual_Fund


# @admin.register(Lic)
# class LicAdmin(ImportExportModelAdmin):
# 	list_display =('email','address_line_one','address_line_two','lendmark','city','state','first_name','last_name','dob','contact','address',
#              'policy_type','policy_number','premium','sum_assured','year_of_policy'
#              ,'beneficiary_name','created_on','renew_date','status')


admin.site.register(Drive)
admin.site.register(Lic)
admin.site.register(PolicyType)
admin.site.register(Lead)
admin.site.register(Discuss)
admin.site.register(Mutual_Fund)
