# Django imports
from django.urls import path

# Local imports
from . import views

urlpatterns = [
    path('api/v1/lists/', views.ListList.as_view(), name='list-list'),
    path('api/v1/lists/<int:pk>/', views.ListTodos.as_view(), name='list-todos'),
    path('api/v1/lists/create/', views.CreateList.as_view(), name='list-create'),
    path('api/v1/lists/create/<int:user_id>/', views.CreateListbyUser.as_view(), name='list-create-by-user'),
    path('api/v1/lists/<int:pk>/detail/', views.ListDetail.as_view(), name='list-detail'),
    path('api/v1/lists/<int:pk>/delete/', views.ListDelete.as_view(), name='list-delete'),
    path('api/v1/lists/<int:pk>/update/', views.ListUpdate.as_view(), name='list-update'),
    path('api/v1/lists/<int:pk>/retrieve-update/', views.ListRetrieveUpdate.as_view(), name='list-retrieve-update'),
]