# from django.http import HttpResponse
# from django.shortcuts import render

# def homePage(request):
#     data={
#         'title':'GEITPL',
#         'bdata':'Welcome to office',
#         'clist' : ["js", "django", "python", "github"],
#         'Alist' : ["A","Z","P","K","F"],
#         'numbers': [10,20,30,40,50],
#         'students_detail':[
#             {'name':'pranjal', 'phone': 1345678988},
#             {'name':'shukla', 'phone': 98745632159}

#         ]
#     }
#     return render(request,"index.html")

# def aboutUs(request):
#     return render(request,"about.html")

# def courses(request):
#     return HttpResponse("welcome to my course")


# def Coursedetail(request,courseid):
#     return HttpResponse(courseid)

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
# from .forms import dummyForm


def first(request):
    data = {
        'title': 'GEITPL',
        'bdata': 'Welcome to office',
        'clist': ["js", "django", "python", "github"],
        'Alist': ["A", "Z", "P", "K", "F"],
        'numbers': [10, 20, 30, 40, 50],
        'students_detail': [
            {'name': 'pranjal', 'phone': 1345678988},
            {'name': 'shukla', 'phone': 98745632159}
        ]
    }
    
    return render(request, "first.html", data)


def homePage(request):
    return render(request, "index.html")

def aboutUs(request):
    return render(request, "about.html")

def contactUs(request):
    return render(request, "contact.html")

def courses(request):
    return HttpResponse("Welcome to my course")

def Coursedetail(request, courseid):
    return HttpResponse(f"Course ID: {courseid}")

def firsttt(request):
    return render(request,"first.html")

def submitform(request):
    return HttpResponse(request)


def userForm(request):
    # form = dummyForm()
    # form_data = {'form':form}
    form_data = {}
    
    try:
        if request.method == "POST":
         name = request.POST.get('name')
         email = request.POST.get('email')
         position = request.POST.get('position')

        if name and email and position:
         return HttpResponseRedirect('/about-us/')
        
        # form_data = {'form': form}
    except:
          pass
    return render(request,"userform.html", {'form_data': form_data})




# def calculator(request):
#     result = None  

#     if request.method == "POST":
#         num1 = request.POST.get("num1")
#         num2 = request.POST.get("num2")
#         operation = request.POST.get("operation")

#         try:
#             num1 = float(num1)
#             num2 = float(num2)

#             if operation == "+":
#                 result = num1 + num2
#             elif operation == "-":
#                 result = num1 - num2
#             elif operation == "*":
#                 result = num1 * num2
#             elif operation == "/":
#                 result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
#             else:
#                 result = "Invalid operation"

#         except ValueError:
#             result = "Invalid input"

#     return render(request, "calculator.html", {"result": result})





def calculator(request):
    if request.method == "POST":
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        operation = request.POST.get("operation")

        try:
            num1 = float(num1)
            num2 = float(num2)

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
            else:
                result = "Invalid operation"

        except ValueError:
            result = "Invalid input"

        return redirect(f"/calculator/?result={result}")  

    result = request.GET.get("result")  
    return render(request, "calculator.html", {"result": result})
