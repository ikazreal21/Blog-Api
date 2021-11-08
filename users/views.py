from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


class CreateUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serial = RegisterUserSerializer(data=request.data)
        if reg_serial.is_valid():
            newuser = reg_serial.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serial.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refesh = request.data['refresh_token']
            token = RefreshToken(refresh)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
