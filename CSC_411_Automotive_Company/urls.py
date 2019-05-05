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
from auto.views import *
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

	# Dealer List
	url(r'^dealer_list/$', dealer_list, name="dealer_list"),

	# Dealer Search
	url(r'^dealer_search/$', dealer_search, name="dealer_search"),

	# Dealer Edit
	path('dealer_edit/<int:dealer_id>', dealer_edit, name="dealer_edit"),

	# Dealer Create
	path('dealer_edit/new', dealer_new, name="dealer_new"),

	# Model List
	url(r'^model_list/$', model_list, name="model_list"),

	# Model Search
	url(r'^model_search/$', model_search, name="model_search"),

	# Model Edit
	path('model_edit/<int:model_id>', model_edit, name="model_edit"),

	# Model Create
	path('model_edit/new', model_new, name="model_new"),


	# Supplier List
	url(r'^auto_admin/supplier_list/$', supplier_list, name="supplier_list"),

	# Supplier Search
	url(r'^auto_admin/supplier_search/$', supplier_search, name="supplier_search"),

	# Supplier Edit
	path('auto_admin/supplier_edit/<int:supplier_id>', supplier_edit, name="supplier_edit"),

	# Supplier Create
	path('auto_admin/supplier_edit/new', supplier_new, name="supplier_new"),

	# Manufacturer List
	url(r'^auto_admin/manufacturer_list/$', manufacturer_list, name="manufacturer_list"),

	# Manufacturer Search
	url(r'^auto_admin/manufacturer_search/$', manufacturer_search, name="manufacturer_search"),

	# Manufacture Edit
	path('auto_admin/manufacturer_edit/<int:manufacturer_id>', manufacturer_edit, name="manufacturer_edit"),

	# Manufacturer Create
	path('auto_admin/manufacturer_edit/new', manufacturer_new, name="manufacturer_new"),

	# Sale List
	url(r'^auto_admin/sale_list/$', sale_list, name="sale_list"),

	# Sale Search
	url(r'^auto_admin/sale_search/$', sale_search, name="sale_search"),

	# Sale Edit
	#path('auto_admin/sale_edit/<int:sale_id>', sale_edit, name="sale_edit"),

	# Sale Create
	path('auto_admin/sale_edit/new', sale_new, name="sale_new"),

	# Reports
	# Top Brands
	url(r'^auto_admin/top_brands_report/$', top_brands_report, name="top_brands_report"),

	url(r'^$', index),
	url(r'^error/$', error),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
