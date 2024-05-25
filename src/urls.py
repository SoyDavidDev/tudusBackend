# Django imports
from django.contrib import admin
from django.urls import path, include

# Local imports
from .views import HomeView

urlpatterns = [

    # Django admin
    path('admin/', admin.site.urls),

    # API Home
    path('', HomeView.as_view(), name='home'),

    # Local apps
    path('', include('applications.user.urls')),
    path('', include('applications.lists.urls')),
    path('', include('applications.todo.urls')),
]
