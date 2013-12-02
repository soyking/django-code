from django.views.generic import TemplateView
from items.models import Item,Photo
from django.template import loader,Context
from django.http import HttpResponse

# class IndexView(TemplateView):

# 	template_name="index.html"
	
# 	def get_context_data(self,**kwargs):
# 		context=super(IndexView,self).get_context_data(**kwargs)
# 		context['item_list']=lambda: Item.objects.all()
# 		return context

def IndexView(request):
	item=Item.objects.all()
	t=loader.get_template("index.html")
	c=Context({'item_list':item})
	return HttpResponse(t.render(c))

# class ItemsView(TemplateView):

# 	template_name="items_list.html"

# 	def get_context_data(self,**kwargs):
# 		context=super(ItemsView,self).get_context_data(**kwargs)
# 		context['object_list']=Item.objects.all()
# 		context['allow_empty']=True
# 		return context

def ItemsView(request):
	item=Item.objects.all()
	t=loader.get_template("items_list.html")
	c=Context({'object_list':item})
	return HttpResponse(t.render(c))

def DetailView(request,object_id):
	item=Item.objects.get(id=object_id)
	t=loader.get_template("items_detail.html")
	c=Context({'object':item})
	return HttpResponse(t.render(c))

def PhotoView(reques,object_id):
	photo=Photo.objects.get(id=object_id)
	t=loader.get_template("photos_detail.html")
	c=Context({'object':photo})
	return HttpResponse(t.render(c))


