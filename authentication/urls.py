from django.urls import path
from .views import Singup


urlpatterns = [
    path('signup/', Singup.as_view(), name='signup'),
]
