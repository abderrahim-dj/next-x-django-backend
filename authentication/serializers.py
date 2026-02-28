from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer(serializers.ModelSerializer):


  password = serializers.CharField(write_only=True)

  class Meta:
    model=CustomUser
    fields = ('id', 'username', 'password')

  def create(self, validated_data):
    user=CustomUser.objects.create_user(
      username=validated_data['username'],
      password=validated_data['password']
    )
    return user
  
  def get_tokens(self, obj):
    refresh = RefreshToken.for_user(obj)
    return {
      'refresh_token': str(refresh),
      'access_token': str(refresh.access_token),
    }