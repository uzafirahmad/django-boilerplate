from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenVerifyView
from authentication import views

urlpatterns = [
    path('access/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('create/', views.create, name='create'),
    path('gettoken/',views.get_tokens_for_user, name='gettoken')
]

