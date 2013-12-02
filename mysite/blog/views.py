# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse
from blog.models import BlogPost
from django.shortcuts import render_to_response

def archive(request):
	posts=BlogPost.objects.all()
	t=loader.get_template("archive.html")
	c=Context({'posts':posts})
	return render_to_response("archive.html",{'posts':posts})
	# return HttpResponse(request.path)
	# return HttpResponse(request.GET['page'])

def test(request):
	return render_to_response("test.html")