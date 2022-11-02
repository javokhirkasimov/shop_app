from rest_framework import generics
from .serializers import EmployeeSerializer
from .models import Employee
# Create your views here.


class ListEmployee(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
