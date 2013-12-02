from django.conf.urls.defaults import *
from blog.views import archive,test

urlpatterns=patterns('',
	url(r'^$',archive),
	url(r'^test/',test),
)