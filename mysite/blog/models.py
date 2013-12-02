from django.db import models
from django.contrib import admin

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    author = models.ForeignKey(Author)
    
    class Meta:
        ordering = ['-timestamp']
    
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp','author')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','id')
    
admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(Author,AuthorAdmin)