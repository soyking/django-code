from django.conf.urls.defaults import *
from pastebin.views import PasteListView,PasteDetailView
from pastebin.models import Paste
from pastebin.form import PasteCreate

urlpatterns = patterns('',
	url(r'^$',PasteListView),
    url(r'^(?P<object_id>\d+)/$', PasteDetailView),
    url(r'^add/$', PasteCreate),
    )