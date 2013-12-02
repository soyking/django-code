from django.http import HttpResponse
from django.core import serializers
from django.views.generic.list import ListView
from liveupdate.models import Update


def UpdatesAfter(request, id):
    response = HttpResponse()
    response['Content-Type'] = "text/javascript" #for correct response and analysis from javascript
    response.write(serializers.serialize("json", Update.objects.filter(pk__gt=id)))
    return response

class UpdateList(ListView):
	model=Update
	def get_context_data(self,**kwarg):
		context=super(UpdateList,self).get_context_data(**kwarg)
		return context
