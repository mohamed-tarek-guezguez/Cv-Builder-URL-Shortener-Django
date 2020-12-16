from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.ejs', extra_context={'title': 'Sign in'}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.ejs', extra_context={'title': 'Logout'}), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
]