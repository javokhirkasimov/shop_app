from django.contrib import admin
from .models import Visit
# Register your models here.


class VisitAdmin(admin.ModelAdmin):
    search_fields = ['outlet__title', 'outlet__employee__name']

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Visit, VisitAdmin)



