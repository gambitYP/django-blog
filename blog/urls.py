from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='index'),
    url(r'^category/(?P<slug>[^\.]+)/$', views.CategoryListView.as_view(), name='category'),
    url(r'^post/add/$', views.PostCreateView.as_view(), name='post-add'),
    url(r'^post/(?P<slug>[^\.]+)/edit/$', views.PostEditView.as_view(), name='post-edit'),
    url(r'^post/(?P<slug>[^\.]+)/delete/$', views.PostDeleteView.as_view(), name='post-delete'),
    url(r'^post/(?P<slug>[^\.]+)/$', views.PostDetailView.as_view(), name='post'),
]