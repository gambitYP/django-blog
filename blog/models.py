from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	category = models.ForeignKey('blog.Category', null=True)

	def __str__(self):
		return '%s' % self.title

	def __unicode__(self):
		return '%s' % self.title

	@models.permalink
	def get_absolute_url(self):
		return ('blog:post', None, {'slug': self.slug})


class Category(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)

	def __str__(self):
		return '%s' % self.title

	def __unicode__(self):
		return '%s' % self.title

	@models.permalink
	def get_absolute_url(self):
		return('blog:category', None, {'slug': self.slug})