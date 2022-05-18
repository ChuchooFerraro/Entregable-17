"""Entregable URL Configuration

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
from re import template
from django.contrib import admin
from django.urls import path
from Familia.views import templatefamilia
from Familia.views import familia_con_loader
from Familia.views import all_family

urlpatterns = [
    path('admin/', admin.site.urls),
    path('familia/',templatefamilia),
    path('flia/',familia_con_loader),
    path('all_family/',all_family),
]