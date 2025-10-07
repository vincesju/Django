# registration/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Full URL will be /registration/api/register/
    path('api/register/', views.register_user, name='register_user'),
]