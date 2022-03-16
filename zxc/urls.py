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
<<<<<<< HEAD
from django.urls import path
from accounts import views as account_views
from django.contrib.auth import views as user_views
=======
from django.urls import path, include
>>>>>>> 436fc1948e6140fa0bd9b9d1694fe8729f948fd9
# hello iskhak

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('register/', account_views.register, name='register'),
    path('profile/', account_views.profile, name='profile'),
    path('login/', user_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', user_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
=======
    path('', include('blog.urls')),
>>>>>>> 436fc1948e6140fa0bd9b9d1694fe8729f948fd9
]
