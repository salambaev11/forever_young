"""zxc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts import views as account_views
from django.contrib.auth import views as user_views
<<<<<<< HEAD
=======

>>>>>>> 08f9af36910983e3d385bcd496d7fe5d6955001e
from django.urls import path, include

# hello iskhak

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', account_views.register, name='register'),
    path('profile/', account_views.profile, name='profile'),
    path('login/', user_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', user_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('', include('blog.urls')),
<<<<<<< HEAD
]
=======
    ]
>>>>>>> 08f9af36910983e3d385bcd496d7fe5d6955001e
