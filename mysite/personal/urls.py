from django.conf.urls import patterns
from django.conf.urls import url
from views import index
from views import pages

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),
    url(r'^(?P<full_slug>(.*))/$', pages, name='serve-page'),
)