from rest_framework import serializers 
from LeadGenerationApp.models import  Employee
from LeadGenerationApp.models import States
from LeadGenerationApp.models import Cities
from LeadGenerationApp.models import Manager
from LeadGenerationApp.models import Customer
class EmployeeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Employee
        fields = ( 'id',
                  'firstname', 
                  'lastname', 
                  'dob', 
                  'gender', 
                  'emailid', 
                  'mobile', 
                  'address',
                  'state',
                  'city', 
                  'designation', 
                  'managerid', 
                  'photograph'
                  )
class StatesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = States
        fields = ( 'id',
                  'stateid', 
                  'statename', 
                  )
        
class CitiesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cities
        fields = ( 'id',
                  'stateid', 
                  'cityid', 
                  'cityname',
                  )

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Manager
        fields = ( 'id',
                  'managerid', 
                  'firstname', 
                  'lastname', 
                  'dob', 
                  'gender', 
                  'emailid', 
                  'mobile', 
                  'address',
                  'state',
                  'city',  
                  'photograph'
                  )

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Customer
        fields = ( 'id', 
                  'firstname', 
                  'lastname', 
                  'dob', 
                  'gender', 
                  'emailid', 
                  'mobile', 
                  'alternatemobile',
                  'organizationname',
                  'address',
                  'state',
                  'city',  
                  'photograph'
                  )