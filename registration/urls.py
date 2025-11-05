from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('users/', views.get_users, name='get_users'), 
    path('users/<int:id>/', views.user_detail, name='user_detail'),  # CHANGED FROM pk TO id
]