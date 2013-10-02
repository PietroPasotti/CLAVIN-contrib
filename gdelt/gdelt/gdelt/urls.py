from django.conf.urls import patterns, include, url

from gdelt.api import GDELTResource


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

gdelt_resource = GDELTResource()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'gdelt.views.home', name='home'),
    url(r'^api/', include(gdelt_resource.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
