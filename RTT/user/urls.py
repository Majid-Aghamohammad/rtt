from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # Token URLs...
    path('token/', jwt_views.TokenObtainPairView.as_view(),  name='token_obtain'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]