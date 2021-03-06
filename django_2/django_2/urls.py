"""django_2 URL Configuration

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
from django.urls import path, re_path
from app import views

urlpatterns = [
    path('', views.index),
    re_path(r'^news', views.news),
    re_path(r'^management', views.management),
    re_path(r'^fact', views.fact),
    re_path(r'^contact', views.contact),
    path('history', views.history),
    re_path(r'^history/(?P<city>\D+)/', views.history),
    path('admin/', admin.site.urls),
]
