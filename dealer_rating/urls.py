# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from sitebase.forms import LoginForm
from sitebase.views import uploadview,download,compare,displayallratings,DealersListView
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('sitebase.urls')),
    url(r'login/$', auth_views.login, {'template_name': 'login.html' , 'authentication_form': LoginForm}),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}),
    url(r'upload/$', uploadview,name = 'upload'),
    url(r'^uploadpage/$', TemplateView.as_view(template_name="upload.html"), name='upload-page'),
    url(r'^gridview/$',displayallratings , name='displayall'),
    url(r'^testview/$',DealersListView.as_view()),
    url(r'download/$',download,name = 'download'),
    url(r'compare/$',compare,name = 'compare')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
