from django.conf.urls import patterns, include, url
from mysite1.views import hello, current_datetime,hours_ahead
from books import views
from django.conf.urls.defaults import *
from books.models import Publisher
# from django.views.generic import list_detail
from django.views.generic.list import ListView
from django.contrib.auth.views import login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

publisher_info = {
    'qeryset': Publisher.objects.all(),
    'template_name': 'publisher_list_page.html'
}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite1.views.home', name='home'),
    # url(r'^mysite1/', include('mysite1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^hello/$',hello),
    (r'^time/$',current_datetime),
    (r'^another-time-page/$',current_datetime),
    (r'^account/login/$', login,{"template_name":"login.html", "next":"hello.html"}),
    (r'^time/plus/(\d{1,2})/$',hours_ahead),
    # (r'^search-form/$',views.search_form),
    (r'search/$',views.search),
    (r'^contact/$',views.contact),
    # (r'^publishers/$', ListView.view_list, publisher_info)


)
