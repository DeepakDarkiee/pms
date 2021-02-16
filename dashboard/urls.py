from django.urls import path
from dashboard import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from dashboard.views import export_data, import_fund,import_data, export_lead, import_lead,export_fund
from django.views.static import serve 



urlpatterns = [
    
    path('index/',views.index, name='index'),


    path('add-mutual-fund/', views.add_mutual_fund,name='add-mutual-fund'),
    path('show-mutual-fund/', views.show_mutual_fund,name='show-mutual-fund'),
    path('edit-fund/<int:id>',views.edit_fund,name='edit-fund'),
    path('update-fund/<int:id>',views.update_fund,name='update-fund'),
    path('delete-fund/<int:id>', views.delete_fund,name='delete-fund'),
    path('view-fund/<int:id>', views.view_fund,name='view-fund'),
    path('export-fund/',export_fund, name="export-fund"), 
    path('import-fund/',import_fund, name="import-fund"), 
    path('search-mutual-fund/',views.SearchFundView.as_view(),name='search-mutual-fund'),
    path('fund-over-due/', views.fund_over_due,name='fund-over-due'), 



    path('lead/', views.add_lead,name='lead'),
    path('manage-lead/',views.manage_lead,name='manage-lead'),
    path('edit-lead/<int:id>',views.edit_lead,name='edit-lead'),
    path('edit-history/<int:id>',views.edit_history,name='edit-history'),
    path('update-history/<int:id>',views.update_history,name='update-history'),
    path('update-lead/<int:id>',views.update_lead,name='update-lead'),
    path('delete-lead/<int:id>', views.delete_lead,name='delete-lead'),
    path('view-lead/<int:id>', views.view_lead,name='view_lead'),
    path('export-lead/',export_lead, name="export-lead"), 
    path('import-lead/',import_lead, name="import-lead"), 
    path('search-lead/',views.SearchLeadView.as_view(),name='search-lead'),
    path('discussion/', views.discussion, name='discussion'),



    path('add_record/', views.add_record, name='add_record'),
    path('show_record/', views.show_record, name='show_record'),
    path('edit_policy/<int:id>', views.edit_policy,name='edit_policy'),
    path('update_policy/<int:id>', views.update_policy,name='update_policy'),
    path('delete_policy/<int:id>', views.delete_policy,name='delete_policy'),
    path('view_policy/<int:id>', views.view_policy,name='view_policy'),
    path('performance/', views.performance, name='performance'),           
    path('search_record/', views.SearchResultsView.as_view(),name='search_record'),
    path('sort_record/', views.sort_record, name='sort_record'),    
    path('export/', export_data, name="export_data"),
    path('import/', import_data, name="import_data"),    
    path('my-drive/', views.my_drive, name='my-drive'),
    path('add-policy/', views.add_policy, name='add-policy'),
    path('delete_drive/<int:id>', views.delete_drive,name='delete_drive'), 
    path('updateRenewDate/', views.updateRenewDate,name='updateRenewDate'), 
    path('updateRenewDateOverDue/', views.updateRenewDateOverDue,name='updateRenewDateOverDue'), 
    path('over_due/', views.over_due,name='over_due'), 
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
   
    
    
]
