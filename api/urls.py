from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from HospitalApp.views import SearchByImageView, UserHistoryView
from api.views import RegisterView, CustomLoginView, CustomTokenObtainPairView

urlpatterns = [
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('login/', CustomLoginView.as_view(), name='custom_login'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('search_by_image/', SearchByImageView.as_view(), name='search_by_image'),
    path('search_history/', UserHistoryView.as_view(), name='search_history'),

]
