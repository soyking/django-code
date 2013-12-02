from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=100)

class Book(models.Model):
	title = models.CharField(max_length=100)
	num_pages = models.IntegerField(max_length=100)
	# authors = models.ManyToManyField(Author)

	def __unicode__(self):
		return self.title

	class Meta:
		abstract = True

class SmithBook(Book):
	authors = models.ManyToManyField(Author,limit_choices_to = {
			'name__endswith','Smith'
		})

	class Meta:
		abstract = False