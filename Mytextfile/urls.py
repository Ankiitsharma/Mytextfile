"""Mytextfile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.home, name= 'name'),
    path('email_v/',views.email_v,name='email_v'),
    path ('textmaster/',views.textmaster, name='textmaster'),
    path('result/', views.result, name='result'),
    path('face_det/',views.face_det, name='face_det' ),
    path('email_check/',views.email_check, name='email_check' ),
]
