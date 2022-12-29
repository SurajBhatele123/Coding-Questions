"""LeadGeneration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path
# from django.conf.urls import url
from LeadGenerationApp import views
from LeadGenerationApp import managerviews
from LeadGenerationApp import customerviews


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^api/employeeinterface',views.EmployeeInterface),
    re_path(r'^api/employeesubmit',views.EmployeeSubmit),
    re_path(r'^api/employeelist',views.Employee_List),
    re_path(r'^api/statelist',views.States_List),
    re_path(r'^api/citylist',views.Cities_List),
    re_path(r'^api/displayallemployee',views.DisplayAllEmployee),
     re_path(r'^api/employeebyid',views.Employee_List_By_Id),
     re_path(r'^api/employeeupdatedelete',views.Employee_Update_Delete),
   
   
   
    re_path(r'^api/managerinterface',managerviews.ManagerInterface),
    re_path(r'^api/managersubmit',managerviews.ManagerSubmit),
    re_path(r'^api/managerlist',managerviews.Manager_List),
    re_path(r'^api/displayallmanager',managerviews.DisplayAllManager),
    re_path(r'^api/managerbyid',managerviews.Manager_List_By_Id),
     re_path(r'^api/managerupdatedelete',managerviews.Manager_Update_Delete),
    
    
    re_path(r'^api/customerinterface',customerviews.CustomerInterface),
    re_path(r'^api/customersubmit',customerviews.CustomerSubmit),
    re_path(r'^api/customerlist',customerviews.Customer_List),
    re_path(r'^api/displayallcustomer',customerviews.DisplayAllCustomer),
    re_path(r'^api/customerbyid',customerviews.Customer_List_By_Id),
     re_path(r'^api/customerupdatedelete',customerviews.Customer_Update_Delete),
]
