from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse

from items.fields import ThumbnailImageField

class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        ordering = ['name']
        
    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('items.views.DetailView',args=[str(self.id)])
        # reverse('path_to_views',argument),return path to some site

class Photo(models.Model):
    item = models.ForeignKey(Item)
    title = models.CharField(max_length=100)
    image = ThumbnailImageField(upload_to='photos')
    caption = models.CharField(max_length=250, blank=True)
        
    class Meta:
        ordering = ['title']
        
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('items.views.PhotoView',args=[str(self.id)])

class PhotoInline(admin.StackedInline):
    model = Photo

class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Item, ItemAdmin)    
admin.site.register(Photo)
