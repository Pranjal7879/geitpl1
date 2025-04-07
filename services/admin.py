from django.contrib import admin
from services.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    
 list_display=('name','email','position')
    # pass


admin.site.register(Employee, EmployeeAdmin)


