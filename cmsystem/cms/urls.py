from django.conf.urls.defaults import *
from cms.models import Story
from cms.views import StoryDetailView, StoryListView, SearchView, category

urlpatterns = patterns('',
    url(r'^category/(?P<slug>[-\w]+)/$', category, name="cms-category"),
    url(r'^search/$', SearchView, name="cms-search"),
)

urlpatterns += patterns('',
    url(r'^(?P<slug>[-\w]+)/$', StoryDetailView,name="cms-story"),
    url(r'^$', StoryListView, name="cms-home"),
)

