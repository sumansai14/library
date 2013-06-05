from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()
#from books import views
urlpatterns = patterns('books.views',
    # Examples:
    url(r'^$', 'index'),
    #url(r'^<book_id>/$' 'book'),
    url(r'^(?P<book_slug>.*)/$', 'book'),
    url(r'^(?P<book_id>.\d+)/return/$', 'return_request'),
    #url(r'^(?P<book_slug>.*)/request/$', 'books.views.request_book'),

    # url(r'^library/', include('library.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
