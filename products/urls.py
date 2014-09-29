from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('products.views',

    url(r'^$','list_all', name ="all_products"),
    url(r'^add/','add_product', name ="add_product"),
	url(r'^(?P<slug>.*)/edit/','edit_product', name ="edit_product"),
	url(r'^(?P<slug>.*)/$','single', name ="single_product"),
    
)
