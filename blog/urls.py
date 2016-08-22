from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='index'),
    url(r'^(?P<slug>[^\.]+)/$', views.PostDetailView.as_view(), name='post'),
    url(r'^post/add/$', views.PostCreate.as_view(), name='post-add'),
]