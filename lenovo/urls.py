"""djangoBegin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include


from lenovo.views import account,views

urlpatterns = [
    # 用户登录url
    path('logined/', views.toIndex, name='indexes'),
    path('login/', account.Login.as_view(), name="login"),
    # 验证码url
    path('get_auth_img/', account.GetAuthImg.as_view(), name="get_auth_img"),
    path('register/', account.Register.as_view(), name="register"),
]
