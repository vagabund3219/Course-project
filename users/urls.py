from django.urls import path
from .views import register
from django.contrib.auth import views
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]
