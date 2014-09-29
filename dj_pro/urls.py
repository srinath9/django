from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$','products.views.list_all', name ="all_products"),
	url(r'^products/', include('products.urls')),
	
    # Examples:
    # url(r'^$', 'dj_pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/',include('django.contrib.admindocs.urls')),
)
