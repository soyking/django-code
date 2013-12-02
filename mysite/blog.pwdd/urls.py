from django.conf.urls.defaults import *
from django.contrib.syndication.views import Feed as feed
from blog.views import archive
from blog.forms import process_form
from blog.feeds import RSSFeed

urlpatterns = patterns('',
    url(r'^$', archive),
    url(r'^feeds/(?P<url>.*)/$', feed, {'feed_dict': {'rss': RSSFeed}}),
    url(r'^forms',process_form)
)
