from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from saki import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^user/$', views.UserView.as_view(), name='user'),
                       )

