from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'note.views.home', name='home'),
    # url(r'^note/', include('note.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^notes/$', 'core.views.index'),
    url(r'^note/$', 'core.views.note_create'),
    url(r'^note/(?P<note_id>\d+)', 'core.views.note_detail'),
    url(r'^note/(?P<note_id>\d+)/update', 'core.views.note_update'),
    url(r'^note/(?P<note_id>\d+)/delete', 'core.views.note_delete'),
)
