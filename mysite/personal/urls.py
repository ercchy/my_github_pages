from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('',
    url(r'^$', 'personal.views.index', name='index'),
)