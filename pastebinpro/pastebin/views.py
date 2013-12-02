from django.views.generic.list import ListView
from pastebin.models import Paste
from django.template import loader,Context
from django.http import HttpResponse
from django.shortcuts import render_to_response

def PasteListView(request):
    if request.POST :
    	a=Paste(title=request.POST['title'],syntax=request.POST['syntax'],poster=request.POST['poster'],content=request.POST['content'])
    	a.save()
    paste=Paste.objects.all()
    return render_to_response("pastebin/paste_list.html",{'object_list':paste})

def PasteDetailView(request,object_id):
	paste=Paste.objects.get(id=object_id)
	t=loader.get_template("pastebin/paste_detail.html")
	c=Context({'object':paste})
	return HttpResponse(t.render(c))
