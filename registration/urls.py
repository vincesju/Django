from django.urls import path
from . import views

urlpatterns = [
    path('api/register/', views.register_user, name='register_user'),
    path('api/users/', views.get_users, name='get_users'), 
]