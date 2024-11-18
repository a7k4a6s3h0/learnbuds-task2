from django.urls import path
from . import views

urlpatterns = [
     path('admin-home/', views.admin_home, name='admin_home'),
     path('create-user/', views.CreateUserView.as_view(), name='create_user'),
     path('update_user/<int:pk>/', views.UpdateUserView.as_view(), name='update_user'),
     path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
     path('view-users/', views.view_users, name='view_users'),
]
