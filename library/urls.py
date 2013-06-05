from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from books.views import loginview
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^books/$', 'books.views.index'),
    #url(r'^books/(?P<book_id>.*)/$', 'books.views.book'),
    #url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    #url(r'^members/', include('members.urls'))
    url(r'^(?P<book_id>\d+)/issue/(?P<user_id>\d+)/$', 'books.views.issue'),    
    url(r'^books/', include('books.urls')),
    url(r'^login/', 'books.views.loginview'),
    url(r'^$', 'books.views.loginview'),
    url(r'^profile/', 'books.views.profile'),
    url(r'^signup/', 'books.views.signup'),
    url(r'^logout/', 'books.views.logout_req'),
    url(r'^request/(?P<book_id>\d+)/$', 'books.views.request_book'),
    url(r'^add_books/', 'books.views.add_books'),
    url(r'^requests/', 'books.views.requests'),

    #url(r'^login/', 'books.views.login'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
