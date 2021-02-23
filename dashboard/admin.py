from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Lic,PolicyType,Drive,Lead,Discuss,Mutual_Fund

###################################################################################################################################################################

admin.site.register(Drive)
admin.site.register(Lic)
admin.site.register(PolicyType)
admin.site.register(Lead)
admin.site.register(Discuss)
admin.site.register(Mutual_Fund)


###################################################################################################################################################################