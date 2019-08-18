"""AttendanceManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),  # urls for admin portal
    path('users/', include('users.urls')),  # urls for users app
    path('users/', include('django.contrib.auth.urls')),  # urls for django user auth
    path('', include('announcements.urls')),  # homepage url
    path('records/', include('records.urls')),  # urls for records app
    path('api/', include('api.urls')),  # urls for api app
    path('api-auth/', include('rest_framework.urls')),  # urls for browsable api auth
    path('api/rest-auth/', include('rest_auth.urls')),  # urls for api auth endpoints 
]


urlpatterns += staticfiles_urlpatterns()