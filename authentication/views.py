from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class IndexView(APIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    return Response({'message': 'test'}, status=status.HTTP_200_OK)
