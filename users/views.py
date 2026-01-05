from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import RegisterSerializer, MeSerializer
# Create your views here.
class RegisterAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

class LoginAPIView(TokenObtainPairView):
    #uses simplejwt default serializer (username + password)
    permission_classes = [permissions.AllowAny]

class RefreshAPIView(TokenRefreshView):
    permission_classes = [permissions.AllowAny]

class MeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(MeSerializer(request.user).data)