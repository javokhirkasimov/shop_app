from rest_framework import serializers
from .models import Employee


class PhoneNumberSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=255, required=True)


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'name', 'phone_number']
