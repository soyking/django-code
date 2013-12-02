from django import forms
from pastebin.models import Paste
from django.shortcuts import render_to_response
from django.template import RequestContext

class PasteForm(forms.ModelForm):
	class Meta:
		model=Paste

def PasteCreate(request):
	form=PasteForm()
	return render_to_response('pastebin/paste_form.html',{'form':form},context_instance=RequestContext(request))