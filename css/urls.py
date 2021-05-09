"""css URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app.views import index,signin,encrypt_file,errorpage,decrypt_file,hash_func,mono,poly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signin,name='login'),
    path('index/',index,name='index'),
    path('mono/',mono,name='mono'),
    path('poly/',poly,name='poly'),
    path('hash/<str:sha>',hash_func,name='hash'),
    path('error/',errorpage,name='errorpage'),
    path('files/encrypt/',encrypt_file,name='encrypt_file'),
    path('files/decrypt/',decrypt_file,name='decrypt_file'),
    
]
