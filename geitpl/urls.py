"""
URL configuration for geitpl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# """
# from django.contrib import admin
# from django.urls import path
# from geitpl import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('about-us/', views.aboutUs),
#     path('', views.homePage),
#     path('course/',views.courses),
#     path('course/<int:courseid>',views.Coursedetail) 
# ]







# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$/

from django.contrib import admin
from django.urls import path
from geitpl import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='home'),
    path('about-us/', views.aboutUs, name='about'),
    path('contact-us/', views.contactUs,name='contact'),
    path('course/', views.courses, name='course'),
    path('course/<int:courseid>/', views.Coursedetail, name='course_detail'),
    path('first/', views.first,name='first'),
    path('userform', views.userForm,name="userform"),
    path('submitform', views.submitform,name="submitform"),

]
