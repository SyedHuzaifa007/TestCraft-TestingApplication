from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='registeration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('translate_to_urdu/', views.translate_to_urdu, name='translate_to_urdu'), 
]
