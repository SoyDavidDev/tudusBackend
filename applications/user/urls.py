# Django imports
from django.urls import path

# Local imports
from . import views

urlpatterns = [
    path('api/v1/users/', views.UserList.as_view(), name='user-list'),
    path('api/v1/users/<int:pk>/', views.UserLists.as_view(), name='user-lists'),
    path('api/v1/users/create/', views.CreateUser.as_view(), name='user-create'),
    path('api/v1/users/<int:pk>/detail/', views.UserDetail.as_view(), name='user-detail'),
    path('api/v1/users/<int:pk>/delete/', views.UserDelete.as_view(), name='user-delete'),
    path('api/v1/users/<int:pk>/update/', views.UserUpdate.as_view(), name='user-update'),
    path('api/v1/users/<int:pk>/retrieve-update/', views.UserRetrieveUpdate.as_view(), name='user-retrieve-update'),
]
