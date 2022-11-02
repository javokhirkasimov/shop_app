from rest_framework import serializers
from .models import Visit


class CreateVisitSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=255, required=True)
    outlet_pk = serializers.IntegerField(required=True)
    latitude = serializers.FloatField(required=True)
    longitude = serializers.FloatField(required=True)


class VisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = ['id', 'date_time']
