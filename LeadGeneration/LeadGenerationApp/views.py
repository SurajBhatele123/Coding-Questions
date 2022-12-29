from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.db import connection
from LeadGenerationApp.models import Employee
from LeadGenerationApp.models import States
from LeadGenerationApp.models import Cities
from LeadGenerationApp.serializers import EmployeeSerializer
from LeadGenerationApp.serializers import StatesSerializer
from LeadGenerationApp.serializers import CitiesSerializer
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from .import tuple_to_dict
from django.shortcuts import redirect


# Create your views here.
@api_view(['GET','POST','DELETE'])
def EmployeeInterface(request):
   return render(request,"Employee.html")
@api_view(['GET','POST','DELETE'])
def EmployeeSubmit(request):
        if request.method == 'POST':
         # employee_data = request.GET.dict()
         print("Employee",request.data)
         employee_serializer = EmployeeSerializer(data=request.data)
        if employee_serializer.is_valid():
           employee_serializer.save()
           return render(request,"Employee.html",{"Message":"Record Submitted Sucessfully"})
           # return JsonResponse({"Message":"Record Submitted Sucessfully"}, status=status.HTTP_201_CREATED)
        return render(request,"Employee.html",{"Message":"Server Error : Fail to Record Submit"})   
        #return JsonResponse({"Message":"Server Error : Fail to Record Submit"}, status=status.HTTP_400_BAD_REQUEST)
'''
@api_view(['GET','POST','DELETE'])
def Employee_List(request):
       if request.method=="GET":
              employee_list=Employee.objects.all()
              print("Empoyee",employee_list)
              employee_serializer = EmployeeSerializer(employee_list,many=True)
              print("Employee",employee_serializer.data)
              return JsonResponse(employee_serializer.data,safe=False)
       return JsonResponse({},safe=False)
 '''

@api_view(['GET','POST','DELETE'])
def Employee_List(request):
       if request.method=="GET":
              cursor=connection.cursor()
              q="select E.*,(select S.statename from leadgenerationapp_states S where S.stateid=E.state) as statename,(select C.cityname from leadgenerationapp_cities C where C.cityid=E.city) as cityname,(select M.firstname from leadgenerationapp_manager M where M.managerid=E.managerid) as mfirstname,(select M.lastname from leadgenerationapp_manager M where M.managerid=E.managerid) as mlastname from leadgenerationapp_employee E"
              cursor.execute(q)
              data=tuple_to_dict.parsetodictAll(cursor) 
              return JsonResponse(data,safe=False)
       return JsonResponse({},safe=False) 


@api_view(['GET','POST','DELETE'])
def Employee_List_By_Id(request):
       if request.method=="GET":
              employeeid=request.GET["employeeid"]
              cursor=connection.cursor()
              q="select E.*,(select S.statename from leadgenerationapp_states S where S.stateid=E.state) as statename,(select C.cityname from leadgenerationapp_cities C where C.cityid=E.city) as cityname,(select M.firstname from leadgenerationapp_manager M where M.managerid=E.managerid) as mfirstname,(select M.lastname from leadgenerationapp_manager M where M.managerid=E.managerid) as mlastname from leadgenerationapp_employee E where E.id={0}".format(employeeid)
              cursor.execute(q)
              data=tuple_to_dict.parsetodictone(cursor) 
              data['dob']=str(data['dob'])
              if data['gender']=='Male' : mg=True
              else : mg=False
              if data['gender']=='Female' : fg=True
              else : fg=False
              return render(request,"EmployeeById.html",{'record':data,'mgender':mg,'fgender':fg})
       return JsonResponse({},safe=False)



@api_view(['GET','POST','DELETE'])
def States_List(request):
       if request.method=="GET":
              state_list=States.objects.all()
              state_serializer = StatesSerializer(state_list,many=True)
              return JsonResponse(state_serializer.data,safe=False)
       return JsonResponse({},safe=False)
    
@api_view(['GET','POST','DELETE'])
def Cities_List(request):
       if request.method=="GET":
              cities_list=Cities.objects.raw("select * from Leadgenerationapp_cities where stateid={0}".format(request.GET['stateid']))
              cities_serializer = CitiesSerializer(cities_list,many=True)
              return JsonResponse(cities_serializer.data,safe=False)
       return JsonResponse({},safe=False)
      
@api_view(['GET','POST','DELETE'])
def DisplayAllEmployee(request):
   return render(request,"DisplayAllEmployee.html")      

@api_view(['GET','POST','DELETE'])
def Employee_Update_Delete(request):
       if request.method=="GET":
         btn=request.GET['btn']
         if(btn=='Edit'):
          employee=Employee.objects.get(pk=request.GET['id'])
          employee.firstname=request.GET['firstname']
          employee.lastname=request.GET['lastname']
          employee.dob=request.GET['dob']
          employee.mobile=request.GET['mobile']
          employee.emailid=request.GET['emailid']
          employee.gender=request.GET['gender']
          employee.address=request.GET['address']
          employee.state=request.GET['state']
          employee.city=request.GET['city']
          employee.designation=request.GET['designation']
          employee.managerid=request.GET['managerid']
          employee.save()
         else:
          employee=Employee.objects.get(pk=request.GET['id'])
          employee.delete()
       return redirect('/api/displayallemployee')