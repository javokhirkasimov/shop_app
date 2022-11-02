from django.urls import path

from .views import ListEmployee

urlpatterns = [
    path('', ListEmployee.as_view(), name='list-employee')
]
