from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from .models import Post, Category


class PostListView(ListView):
	template_name = 'blog/index.html'
	context_object_name = 'posts'
	paginate_by = 3

	def get_context_data(self, **kwargs):
		context = super(PostListView, self).get_context_data(**kwargs)
		context['cats'] = Category.objects.all()
		return context

	def get_queryset(self):
		return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post.html'


class PostCreate(CreateView):
	model = Post
	fields = ['author', 'title', 'text', 'created_date', 'published_date']


class CategoryListView(ListView):
	template_name = 'blog/category.html'
	context_object_name = 'posts'
	paginate_by = 5

	def get_context_data(self, **kwargs):
		context = super(CategoryListView, self).get_context_data(**kwargs)
		context['category'] = Category.objects.get(slug = self.kwargs['slug'])
		return context

	def get_queryset(self):
		return Post.objects.filter(published_date__lte=timezone.now()).filter(category__slug=self.kwargs['slug']).order_by('-published_date')
