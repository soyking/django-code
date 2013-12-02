from django.conf.urls.defaults import *
from liveupdate.views import UpdatesAfter,UpdateList
from liveupdate.models import Update

urlpatterns = patterns('',
    url(r'^$', UpdateList.as_view()),
    url(r'^updates-after/(?P<id>\d+)/$', UpdatesAfter),
)
