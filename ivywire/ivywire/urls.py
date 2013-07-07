from django.conf.urls import *
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'direct_to_template, {
	#	'template': '/ivywire/index.html'
	#}),
    # url(r'^ivywire/', include('ivywire.foo.urls')),
	
	(r'^$', TemplateView.as_view(template_name='index.html')),
	(r'^apps/', TemplateView.as_view(template_name='apps.html')),
	(r'^web/', TemplateView.as_view(template_name='web.html')),
	(r'^contact/', TemplateView.as_view(template_name='contact.html')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
