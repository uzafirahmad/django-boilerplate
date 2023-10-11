from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenVerifyView
from authentication import views

urlpatterns = [
    # payload must contain "email" and "password". This is a POST api which returns "access" and "refresh" in it's payload
    path('access/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    # payload must contain "refresh". This is a POST api which returns a new "access" and "refresh" in it's payload
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # payload must contain "token" and this will have the access token. This is a POST api which has tells if token is valid
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),


    path('create/', views.create, name='create'),
]

