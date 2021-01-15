from django.urls import path
from home import views


urlpatterns = [

   	path('', views.home, name='home'),
	#path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),   
    path('digital_pms/',views.digital_pms,name='digital_pms'), 
   
]
