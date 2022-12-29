from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.db import connection
from LeadGenerationApp.models import Employee
from LeadGenerationApp.models import States
from LeadGenerationApp.models import Cities
from LeadGenerationApp.models import Customer
from LeadGenerationApp.serializers import EmployeeSerializer
from LeadGenerationApp.serializers import StatesSerializer
from LeadGenerationApp.serializers import CitiesSerializer
from  LeadGenerationApp.serializers import CustomerSerializer
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from LeadGenerationApp import tuple_to_dict
from django.shortcuts import  redirect

@api_view(['GET','POST','DELETE'])
def CustomerInterface(request):
   return render(request,"Customer.html")

@api_view(['GET','POST','DELETE'])
def CustomerSubmit(request):
        if request.method == 'POST':
         # customer_data = request.GET.dict()
         print("Customer",request.data)
         customer_serializer = CustomerSerializer(data=request.data)
        if customer_serializer.is_valid():
           customer_serializer.save()
           return render(request,"Customer.html",{"Message":"Record Submitted Sucessfully"})
           # return JsonResponse({"Message":"Record Submitted Sucessfully"}, status=status.HTTP_201_CREATED)
        return render(request,"Customer.html",{"Message":"Server Error : Fail to Record Submit"})  
        #return JsonResponse({"Message":"Server Error : Fail to Record Submit"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST','DELETE'])
def Customer_List(request):
       if request.method=="GET":
              cursor=connection.cursor()
              q="select U.*,(select S.statename from leadgenerationapp_states S where S.stateid=U.state) as statename,(select C.cityname from leadgenerationapp_cities C where C.cityid=U.city) as cityname from leadgenerationapp_customer U"
              cursor.execute(q)
              data=tuple_to_dict.parsetodictAll(cursor) 
              return JsonResponse(data,safe=False)
       return JsonResponse({},safe=False)
    
@api_view(['GET','POST','DELETE'])
def Customer_List_By_Id(request):
       if request.method=="GET":
              customerid=request.GET["customerid"]
              cursor=connection.cursor()
              q="select U.*,(select S.statename from leadgenerationapp_states S where S.stateid=U.state) as statename,(select C.cityname from leadgenerationapp_cities C where C.cityid=U.city) as cityname from leadgenerationapp_customer U where U.id={0}".format(customerid)
              cursor.execute(q)
              data=tuple_to_dict.parsetodictone(cursor) 
              data['dob']=str(data['dob'])
              if data['gender']=="Male" :  mg=True
              else: mg=False
              if data['gender']=="Female" : fg=True
              else: fg=False
              return render(request,"CustomerById.html",{'record':data, 'mgender':mg, 'fgender':fg})
       return JsonResponse({},safe=False)


@api_view(['GET','POST','DELETE'])
def DisplayAllCustomer(request):
   return render(request,"DisplayAllCustomer.html")


@api_view(['GET','POST','DELETE'])
def Customer_Update_Delete(request):
       if request.method=="GET":
         btn=request.GET['btn']
         if(btn=='Edit'):
          customer=Customer.objects.get(pk=request.GET['id'])
          customer.firstname=request.GET['firstname']
          customer.lastname=request.GET['lastname']
          customer.dob=request.GET['dob']
          customer.mobile=request.GET['mobile']
          customer.emailid=request.GET['emailid']
          customer.gender=request.GET['gender']
          customer.address=request.GET['address']
          customer.state=request.GET['state']
          customer.city=request.GET['city']
          customer.alternatemobile=request.GET['alternatemobile']
          customer.organizationname=request.GET['organizationname']
          
          customer.save()
         else:
          customer=Customer.objects.get(pk=request.GET['id'])
          customer.delete()
       return redirect('/api/displayallcustomers')