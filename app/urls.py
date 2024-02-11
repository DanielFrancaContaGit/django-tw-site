"""app URL Configuration

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
from django.conf import settings

from . import views

from django.urls import include, path
from rest_framework import routers

from core import views as coreViews

router = routers.DefaultRouter()
router.register(r'users', coreViews.UserViewSet)
router.register(r'groups', coreViews.GroupViewSet)

urlpatterns = [
    path('', views.home_view, name='home'),
    path('coxinha/', views.homedelete, name='coxinha'),
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
