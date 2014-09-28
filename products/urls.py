from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('products.views',

    url(r'^$','list_all', name ="all_products"),
	url(r'^(?P<slug>.*)$','single', name ="single_product"),
    
)
