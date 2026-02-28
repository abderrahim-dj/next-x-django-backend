from .models import CustomUser


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer


# Register your models here.


class Singup(APIView):
  def post(self, request):

    print(request.data)

    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()

      jwt_tokens = RefreshToken.for_user(user)

      return Response({
        'message': 'user created successfully',
        'user': serializer.data,
        'access_token': str(jwt_tokens),
        'refresh_token': str(jwt_tokens.access_token)
      },
        status=status.HTTP_201_CREATED
      )
  
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
