from django import forms
from django.shortcuts import render_to_response

class PersonForm(forms.Form):
	first = forms.CharField(max_length=100,required=True)
	last = forms.CharField(max_length=100,required=True,initial='Smith',widget=forms.PasswordInput())
	middle = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'size':3}))

def process_form(request):
	if not request.POST:
		form = PersonForm(initial = {'first':'John'},auto_id=False)
		return render_to_response('forms.html',{'form':form})