# -*- coding: utf-8 -*- 

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("",
    #url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r'^$', 'reviews.views.home', name='home'),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^dashboard", 'reviews.views.dashboard'),
    url('^accounts/', include('registration.urls')),
    url('^accounts/login/$', 'reviews.views.login'),
    url('^accounts/auth/$', 'reviews.views.auth_view'),
    url('^accounts/logout/$', 'django.contrib.auth.views.logout'),
    #produt
    #url(r'^(?P<slug>.*)/$', 'single_product'),
    url(r'^(?P<slug>[^/]+)/$', 'reviews.views.single_product'),
    #submit reviews
    url('^(?P<slug>[^/]+)/review_submit/$','reviews.views.single_product'),
    #search
    url(r'^search/$', 'reviews.views.search'),
    
)

