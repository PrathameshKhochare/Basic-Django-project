from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework import permissions, viewsets
from pathlib import Path
from .models import Company , Employee
from .serializers import CompanySerializer ,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
# Functions or classes which mappes to url's

# def index(request):
#     print("Home page")
#     friends = [
#         'Ravi','Mahesh' ,'Guru' ,'Ramesh'
#     ]
#     #return HttpResponse("<h1>Welcome to the Prathamesh's Study Planner setup<h1/>")
#     return JsonResponse(friends,safe= False)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class  = CompanySerializer

    # companies/{company_id}/employees
    @action(detail=True , methods = ['get'])
    def employees(self,request,pk =None):
        print("get employees of ",pk ,"company")

        try:
            company = Company.objects.get(pk = pk)
            emps = Employee.objects.filter(company = company)
            emps_serializer = EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({'message':"Comapany might not exit !! error!!!"})



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class  = EmployeeSerializer
