"""quiz_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [
    path('',views.login_function,name='loginpage'),
    path('quiz',views.quiz,name='quizpage'),
    path('signup',views.signup.as_view(),name='signuppage'),
    path('logout',views.logout_function, name="logoutpage"),
    path('getdata',views.get_data,name='get_datapage'),
    path('postdata',views.post_data,name='post_datapage'),
    path('test',views.test,name='testpage'),




    
]
