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
    url(r'^accounts/register_user/$', "products.views.register_user" ),
    url(r'^accounts/register_success/$', "products.views.register_success" ),
    url(r'^accounts/login_user/$', "products.views.login_user" ),
    url(r'^accounts/login_success/$', "products.views.loggin_success" ),
    url(r'^accounts/logout/$', "products.views.logout" ),
    url(r'^accounts/auth/$', "products.views.auth_view" ),
    url(r'^accounts/invalid/$', "products.views.invalid" ),
    url(r'^file_uploads/$',"products.views.file_upload")
)
