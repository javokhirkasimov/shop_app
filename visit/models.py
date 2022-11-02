from django.db import models
from outlet.models import Outlet
# Create your models here.


class Visit(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.outlet} | {self.date_time}"
