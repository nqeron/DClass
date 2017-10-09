"""class_reg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.HomePage.as_view(),name='home'),
    url(r'^login_success/$',views.LoginSuccessPage.as_view(),name='login_success'),
    url(r'^leave/$',views.LeavePage.as_view(),name='leave'),
    url(r'^students/', include('students.urls',namespace='students')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # url(r'^students/', include('students.urls',namespace='students')),
    # url(r'^students/', include('django.contrib.auth.urls')),
    url(r'^school_classes/',include("school_class.urls",namespace="classes")),
]
