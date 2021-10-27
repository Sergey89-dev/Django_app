"""geekshop URL Configuration

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
from django.urls import path
from django.urls.conf import include
from mainapp import views as mainapp
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('contact/', mainapp.contact, name='contact'),
    path('products/', mainapp.products, name='products'),
    path('admin/', admin.site.urls),
    path('products/home/', mainapp.products_home, name='products_home'),
    path('products/office/', mainapp.products_office, name='products_office'),
    path('products/classic/', mainapp.products_classic, name='products_classic'),
    path('products/modern/', mainapp.products_modern, name='products_modern'),
    path('auth/', include('authapp.urls', namespace = 'auth'))
]

if settings.DEBUG:
    urlpatterns += static