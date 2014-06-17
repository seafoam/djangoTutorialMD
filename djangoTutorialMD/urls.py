from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoTutorialMD.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #Code Coverage
    url(r'^htmlcov/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/orc/LEARN/djangoTutorialMD/htmlcov/', 'show_indexes': True}),

    # Blog URLs
    url(r'', include('blogengine.urls')),
        
   # Flat pages
    url(r'', include('django.contrib.flatpages.urls')),
    
    
)
