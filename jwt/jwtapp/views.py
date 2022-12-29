from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.db import connection
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from jwtapp.serializer import AuthenticationSerializer
from jwtapp.models import Authentication
from django.shortcuts import redirect


# Create your views here.

@api_view(['GET','POST','DELETE'])
def LoginInterface(request):
   return render(request,"auth.html")

@api_view(['GET','POST','DELETE'])
def Auth_Login(request):
        if request.method == 'GET':
            login_data = request.GET.dict()
            print(login_data)
            auth_serializer = AuthenticationSerializer(data=login_data)
        if auth_serializer.is_valid():
           print(auth_serializer)
           auth_serializer.save()
           return render(request,"auth.html",{"Message":"Login Sucessfully"})
        return render(request,"auth.html",{"Message":"Server Error : Login Fail"})   
       