
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from saki import views

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^saki/', include('saki.urls', namespace="saki")),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^user/$', views.UserView.as_view(), name='user'),
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.STATIC_ROOT}),
                       )