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
from .models import Quiz_Table, QuizAnswers, QuizCorrectAnswers, QuizQuestions




# Create your views here.


# This function is used to Quiz game
from django.contrib.auth import authenticate,login, logout

from app1 import serializers
from django.http import JsonResponse


@login_required(login_url='/')
def quiz(request):
    print("------------------quizzzz", request.GET)
    #obj=Quiz_Table.objects.all()

    """_summary_

    [
        {
            'question':'Whats python',
            'options' : [
                {
                    option_text: 'Interpreted language',
                    option_value: 'Interpreted language',
                    is_correct: True
                },
                {
                    option_text: 'Like Java',
                    option_value: 'Like Java',
                    is_correct: False
                }
            ],
            correct_option: [
                {
                    option_text: 'Interpreted language',
                    option_value: 'Interpreted language',
                    is_correct: True
                }
            ]
        }
    ]

    """
    q = request.GET.get('q')
    if q:
        list_of_questions = []
        quiz_question_objects = QuizQuestions.objects.all()
        for question_object in quiz_question_objects:
            temp_dict={
                'question': '',
                'option_list' : [],
                'correct_option':[]
            }
            temp_dict['question'] = question_object.question_text

            # Getting All Options
            option_list = []
            options=QuizAnswers.objects.filter(question=question_object)
            for option in options:
                option_list.append(
                    {
                        'option_text': option.answer_text,
                        'option_value': option.answer_value
                    }
                )
            temp_dict['option_list'] = option_list

            # Getting correct options
            correct_option_list = []
            correct_options = options.filter(is_correct=True)
            for correct_option  in correct_options:
                correct_option_list.append(
                    {
                        'option_text': correct_option.answer_text,
                        'option_value': correct_option.answer_value
                    }
                )
            
            temp_dict['correct_option'] = correct_option_list



            list_of_questions.append(temp_dict)
        print("list_of_questions => ",list_of_questions)
        return JsonResponse(list_of_questions, safe=False)
      
    
    return render(request,'app1/try.html',{'obj':[]})




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


def quizpy(request):
    obj=Quiz_Table.objects.all()
    return render(request,'app1/quizpy.html',{'obj':obj})



