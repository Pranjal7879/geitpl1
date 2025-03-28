from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data={
        'title':'GEITPL',
        'bdata':'Welcome to office',
        'clist' : ["js", "django", "python", "github"],
        'numbers': [10,20,30,40,50],
        'students_detail':[
            {'name':'pranjal', 'phone': 1345678988},
            {'name':'shukla', 'phone': 98745632159}

        ]
    }
    return render(request,"index.html",data)

def aboutUs(request):
    return HttpResponse("this is my home page ")

def courses(request):
    return HttpResponse("welcome to my course")


def Coursedetail(request,courseid):
    return HttpResponse(courseid)