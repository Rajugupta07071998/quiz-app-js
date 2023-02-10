from http.client import HTTPResponse
from pickletools import read_bytes8
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import  io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView




# Create your views here.


# This function is used to Quiz game
from django.contrib.auth import authenticate,login, logout

from app1 import serializers


@login_required(login_url='/')
def quiz(request):
    print("------------------quizzzz")

    return render(request,'app1/try.html')



# This function is used to Signup and save data in User table
class signup(TemplateView):
    template_name = 'app1/signup.html'
    
    def get(self,request, *args, **kwargs):
        return render(request,self.template_name)

    def post(self,request, *args, **kwargs):
    
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']

        x=User.objects.create_user(username=name,email=email,password=password)
        x.save()
        login(request,x)
        print("created successfully")
        print("------------------successfully")
        return redirect('app1:quizpage')
        #return render(request, self.template_name)



# This function is used to login authentication
#from django.contrib import auth

def login_function(request):
    if request.method == 'POST':
        name=request.POST['name']
        password=request.POST['password1']
        #x=auth.authenticate(email=email,password=password)
        user = authenticate(request,username=name,password=password)
        print(user)
        if user is not None:
            print("--------------------------")
            login(request, user)
            return redirect('app1:quizpage')
        else:
            #return ('app1:signuppage')
             #name=request.POST['name']
             #password=request.POST['password1']
             return render(request,'app1/login_error.html',{'name':name,'password':password})
    else:
        
 
         return render(request,'app1/login.html')


def logout_function(request):
    logout(request)
    return redirect('app1:loginpage')

def get_data(request):
    x=User.objects.all()
    serializer=UserSerializer(x,many=True)
    j_data=JSONRenderer().render(serializer.data)
    print(j_data)
    return HttpResponse(j_data,content_type='application/json')



@csrf_exempt
def post_data(request):
    if request.method == 'POST':
        data=request.body
        stream=io.BytesIO(data)
        p_data=JSONParser().parse(stream)
        serializer=UserSerializer(data=p_data)
        if serializer.is_valid():
            serializer.save()

            d={'msg':'data aaya hai'}
            j_data=JSONRenderer().render(d.data)
            return HttpResponse(j_data,content_type='application/json')


def test(request):
    return render(request,'app1/test.html')



