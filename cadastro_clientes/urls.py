from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from django.contrib import admin
from core import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cadastro_clientes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^cadastro/', include('core.urls')),
    #url(r'^teste', include('core.urls')),
)

if settings.DEBUG:                                                              
    urlpatterns += patterns('',                                                 
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),         
    )                                                                           
                                                                                
                                                                                
urlpatterns += staticfiles_urlpatterns() 
