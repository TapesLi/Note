from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('core.views',
    # Examples:
    # url(r'^$', 'note.views.home', name='home'),
    # url(r'^note/', include('note.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'index'),
    url(r'^note$', 'index'),
    url(r'^notes', 'notes_list'),
    url(r'^note/save', 'note_save'),
    url(r'^note/(?P<note_url>\w{8})$', 'note_detail'),
    url(r'^note/(?P<note_url>\w{8})/delete', 'note_delete'),
)
