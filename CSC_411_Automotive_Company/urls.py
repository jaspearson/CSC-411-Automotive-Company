"""CSC_411_Automotive_Company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from auto.views.views import *
from auto.views.customer_view import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^auto_admin/$', auto_admin, name="auto_admin"),

    # Customer List
    url(r'^customer_list/$', customer_list, name="customer_list"),

    # Customer Search
    url(r'^customer_search/$', customer_search, name="customer_search"),

    # Customer Edit
    path('customer_edit/<int:userid>', customer_edit, name="customer_edit"),

    # Customer Create
    path('customer_edit/new', customer_new, name="customer_new"),
    url(r'^$', index),
    url(r'^error/$', error),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
