# Django imports
from django.urls import path

# Local imports
from . import views

urlpatterns = [
    path('api/v1/todos/', views.TodoList.as_view(), name='todo-list'),
    path('api/v1/todos/<int:pk>/', views.TodoDetail.as_view(), name='todo-detail'),
    path('api/v1/todos/create/', views.TodoCreate.as_view(), name='todo-create'),
    path('api/v1/todos/<int:pk>/delete/', views.TodoDelete.as_view(), name='todo-delete'),
    path('api/v1/todos/<int:pk>/update/', views.TodoUpdate.as_view(), name='todo-update'),
    path('api/v1/todos/<int:pk>/retrieve-update/', views.TodoRetrieveUpdate.as_view(), name='todo-retrieve-update'),
]