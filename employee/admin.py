from django.contrib import admin
from .models import Employee
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Employee, EmployeeAdmin)
