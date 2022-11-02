from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OutletSerializer
from employee.serializers import PhoneNumberSerializer
from .models import Outlet
# Create your views here.


class OutletListView(APIView):
    serializer_class = PhoneNumberSerializer

    def post(self, request):
        serializer = PhoneNumberSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            phone_number = request.data.get('phone_number')
            outlets = Outlet.objects.filter(employee__phone_number=phone_number)
            serializer = OutletSerializer(outlets, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
