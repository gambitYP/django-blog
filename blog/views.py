from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


class PostListView(ListView):
	template_name = 'blog/index.html'
	context_object_name = 'posts'
	paginate_by = 1

	def get_queryset(self):
		return Post.objects.order_by('published_date')

		