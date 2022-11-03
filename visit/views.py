from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateVisitSerializer, VisitSerializer
from outlet.models import Outlet
from .models import Visit

# Create your views here.


class CreateVisitView(GenericAPIView):
    serializer_class = CreateVisitSerializer

    def post(self, request):
        serializer = CreateVisitSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            phone_number = request.data.get('phone_number')
            outlet_pk = request.data.get('outlet_pk')
            latitude = request.data.get('latitude')
            longitude = request.data.get('longitude')
            outlet = Outlet

            try:
                outlet = outlet.objects.get(id=outlet_pk)
            except Outlet.DoesNotExist:
                return Response({"error": "Outlet does not exists"}, status=status.HTTP_404_NOT_FOUND)

            if outlet.employee.phone_number == phone_number:
                visit = Visit.objects.create(
                    outlet=outlet,
                    latitude=latitude,
                    longitude=longitude
                )
                serializer = VisitSerializer(visit)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Wrong number"}, status=status.HTTP_404_NOT_FOUND)
