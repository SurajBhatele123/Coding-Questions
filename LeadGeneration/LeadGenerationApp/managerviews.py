from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from  django.db import connection
from LeadGenerationApp.models import Employee
from LeadGenerationApp.models import States
from LeadGenerationApp.models import Cities
from LeadGenerationApp.models import Manager
from LeadGenerationApp.serializers import EmployeeSerializer
from LeadGenerationApp.serializers import StatesSerializer
from LeadGenerationApp.serializers import CitiesSerializer
from LeadGenerationApp.serializers import ManagerSerializer
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from .import tuple_to_dict
from django.shortcuts import redirect

# Create your views here.
@api_view(['GET','POST','DELETE'])
def ManagerInterface(request):
   return render(request,"Manager.html")

@api_view(['GET','POST','DELETE'])
def ManagerSubmit(request):
        if request.method == 'POST':
         # manager_data = request.GET.dict()
         print("Employee",request.data)
         manager_serializer = ManagerSerializer(data=request.data)
        if manager_serializer.is_valid():
           manager_serializer.save()
           return render(request,"Manager.html",{"Message":"Record Submitted Sucessfully"})
           # return JsonResponse({"Message":"Record Submitted Sucessfully"}, status=status.HTTP_201_CREATED)
        return render(request,"Manager.html",{"Message":"Server Error : Fail to Record Submit"})  
        #return JsonResponse({"Message":"Server Error : Fail to Record Submit"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
def Manager_List(request):
       if request.method=="GET":
              cursor=connection.cursor()
              q="select M.*,(select S.statename from leadgenerationapp_states S where S.stateid=M.state) as statename,(select C.cityname from leadgenerationapp_cities C where C.cityid=M.city) as cityname from leadgenerationapp_manager M"
              cursor.execute(q)
              data=tuple_to_dict.parsetodictAll(cursor)
              return JsonResponse(data,safe=False)
       return JsonResponse({},safe=False)
    
@api_view(['GET','POST','DELETE'])
def Manager_List_By_Id(request):
       if request.method=="GET":
              managerid=request.GET["managerid"]
              cursor=connection.cursor()
              q="select M.*,(select S.statename from leadgenerationapp_states S where S.stateid=M.state) as statename,(select C.cityname from leadgenerationapp_cities C where C.cityid=M.city) as cityname from leadgenerationapp_manager M where M.managerid={0}".format(managerid)
              cursor.execute(q)
              data=tuple_to_dict.parsetodictone(cursor)
              data['dob']=str(data['dob'])
              if data['gender']=="Male" : mg=True
              else: mg=False
              if data['gender']=="Female" : fg=True
              else: fg=False
              return render(request,"ManagerById.html",{'record':data, 'mgender':mg, 'fgender':fg})
       return JsonResponse({},safe=False)
    
@api_view(['GET','POST','DELETE'])
def DisplayAllManager(request):
   return render(request,"DisplayAllManager.html") 


@api_view(['GET','POST','DELETE'])
def Manager_Update_Delete(request):
       if request.method=="GET":
         btn=request.GET['btn']
         if(btn=='Edit'):
          manager=Manager.objects.get(pk=request.GET['id'])
          manager.firstname=request.GET['firstname']
          manager.lastname=request.GET['lastname']
          manager.dob=request.GET['dob']
          manager.mobile=request.GET['mobile']
          manager.emailid=request.GET['emailid']
          manager.gender=request.GET['gender']
          manager.address=request.GET['address']
          manager.state=request.GET['state']
          manager.city=request.GET['city']
          manager.save()
         else:
          manager=Manager.objects.get(pk=request.GET['id'])
          manager.delete()
       return redirect('/api/displayallmanager')