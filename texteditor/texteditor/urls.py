from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), 
    path('accounts/login/', LoginView.as_view(template_name='registeration/login.html'), name='login'),
]
