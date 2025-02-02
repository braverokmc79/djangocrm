"""
URL configuration for djangocrm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls.conf import include
from sales.views import 첫화면, 첫화면View
from django.contrib.auth.views import LoginView, LogoutView
from sales.views import CustomLogoutView , 회원가입View


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', 첫화면View.as_view()),
    path('홈페이지/', include('sales.urls', namespace='홈페이지')),
    path('로그인/', LoginView.as_view(), name='로긴'),
    path('로그아웃/', CustomLogoutView.as_view(), name='록아웃'),
    path('회원가입/', 회원가입View.as_view(), name='가입'),
]

