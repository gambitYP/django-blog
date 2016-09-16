from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
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


class PostCreateView(CreateView):
	model = Post
	template_name = 'blog/post_add.html'
	fields = ['title', 'slug', 'text', 'published_date', 'category']

	def form_valid(self, form):
		form.instance.author = self.request.user
		form.instance.created_date = timezone.now()
		return super(PostCreateView, self).form_valid(form)

	def dispatch(self, request, *args, **kwargs):
		if (request.user == None) or not (request.user.is_staff):
			return redirect('blog:index')
		return super(PostCreateView, self).dispatch(request, *args, **kwargs)


class PostEditView(UpdateView):
	model = Post
	template_name = 'blog/post_edit.html'
	fields = ['author', 'title', 'slug', 'text', 'published_date', 'category']


class PostDeleteView(DeleteView):
	model = Post
	template_name = 'blog/post_delete.html'
	success_url = reverse_lazy('blog:index')


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
