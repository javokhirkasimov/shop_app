from django.db import models
from employee.models import Employee
# Create your models here.


class Outlet(models.Model):
    title = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
