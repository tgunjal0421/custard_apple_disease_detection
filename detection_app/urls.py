# detection_app/urls.py
from django.urls import path
from .views import home, predict, history, register, user_login, user_logout, disease_info

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', home, name='home'),
    path('upload/', predict, name='upload'),
    path('history/', history, name='history'),
    path('disease-info/<str:disease_name>/', disease_info, name='disease_info'),
]

