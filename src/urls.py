# Django imports
from django.contrib import admin
from django.urls import path, include

# Rest Framework imports
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token

# Local imports
from .views import HomeView
from applications.user.views import CustomTokenObtainPairView

urlpatterns = [

    # Django admin
    path('admin/', admin.site.urls),

    # API Home
    path('', HomeView.as_view(), name='home'),

    # JWT Authentication
    path('api/v1/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Token Authentication
    path('api/v1/token-auth/', obtain_auth_token, name='api_token_auth'),

    # Local apps
    path('', include('applications.user.urls')),
    path('', include('applications.lists.urls')),
    path('', include('applications.todo.urls')),
]
