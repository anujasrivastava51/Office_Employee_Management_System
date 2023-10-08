from django.shortcuts import render,HttpResponse
from .models import *
from datetime import datetime 
from django.db.models import Q
# Create your views here.

def index(Request):
    return render(Request,'index.html')

def all_emp(Request):
    emps = Employee.objects.all()
    context={
       "emps" : emps
    }
    return render(Request,'view_all_emp.html',context)

def add_emp(Request):
    if(Request.method=="POST"):
        first_name = Request.POST["first_name"]
        last_name = Request.POST["last_name"]
        dept = int(Request.POST["dept"])
        salary =int(Request.POST["salary"]) 
        bonus = int(Request.POST["bonus"])
        role = Request.POST["role"]
        phone = int(Request.POST["phone"])
        hire_date = Request.POST["hire_date"]
        new_emp = Employee(first_name=first_name,last_name=last_name,salary=salary,phone=phone,bonus=bonus,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully")
    elif(Request.method=="GET"):
        return render(Request,'add_emp.html')
    else:
        return HttpResponse("An Exception occured! Employee has not been added")

       

def remove_emp(Request,emp_id=0):
    if emp_id:
        try:
           emp_to_be_removed = Employee.objects.get(id=emp_id)
           emp_to_be_removed.delete()
           return HttpResponse("Employee remover Successfully")
        except:
            return HttpResponse("Please Enter a valid Employee Id")
    emps = Employee.objects.all()
    context={
        "emps":emps
    }
    return render(Request,'remove_emp.html',context)

def filter_emp(Request):
    if Request.method == "POST":
        name = Request.POST["name"]
        dept =Request.POST["dept"]
        role = Request.POST["role"]
        emps = Employee.objects.all()
        if name:
          emps=emps.filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))
        if dept:
          emps=emps.filter(dept__name__icontains=dept)
        if role:
          emps=emps.filter(role__name__icontains=role)
    
        context={
          "emps":emps
        }
        return render(Request,'view_all_emp.html',context)
    elif Request.method=="GET":
       return render(Request,'filter_emp.html')
    else: 
        return HttpResponse('An exceptional occured')
       

