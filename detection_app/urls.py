# detection_app/urls.py
from django.urls import path
from .views import home, predict, history, register, user_login, user_logout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', home, name='home'),  # Home page
    path('upload/', predict, name='upload'),  # Upload & Prediction
    path('history/', history, name='history'),
]
