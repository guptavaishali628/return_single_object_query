from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def home(request):
    # data=Student.objects.create(stu_name='prerna',stu_email='prena@gmail.com',stu_city='indore') always create from this
    # data=Student.objects.first()
    # data=Student.objects.last()
    # print(data.id)
    # print(data.stu_name)
    # print(data.stu_email)
    # print(data.stu_city)
    
    # data=Student.objects.get(stu_city='indore').delete()
    # data=Student.objects.filter(stu_city='indore').delete()
    # data=Student.objects.filter(stu_city='bhopal').update(stu_name='bhavna')
    # data=Student.objects.order_by(stu_name='bhavna')#for ascending order
    # data=Student.objects.order_by(-stu_name='bhavna')#for decending order
    # data=Student.objects.order_by(stu_name[1:2])
    
   
    print("data done successfully")
    return HttpResponse("done!")                                                                
    
    

# return HttpResponse("Welcome to home page")
    