from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url ( r'^media/(?P<path>.*)$', 'django.views.static.serve', name = 'media', kwargs = { 'document_root' : settings.MEDIA_ROOT } ),
    (r'user/', include ( 'userprofile.urls.en' ) ),
    (r'', include('pybbs.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
