from django.contrib import admin
from .models import Outlet
# Register your models here.


class OutletAdmin(admin.ModelAdmin):
    search_fields = ["title"]


admin.site.register(Outlet, OutletAdmin)
