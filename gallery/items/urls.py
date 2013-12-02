from django.conf.urls.defaults import *
from items.views import *

urlpatterns = patterns('',
    # url(r'^$',IndexView.as_view(),name='home'),
    url(r'^$',IndexView,name='home'),
    url(r'^items/$',ItemsView,name='list'),
    url(r'^items/(?P<object_id>\d+)/$',DetailView,name='detail'),
    url(r'^photos/(?P<object_id>\d+)/$',PhotoView,name='photo'),
)