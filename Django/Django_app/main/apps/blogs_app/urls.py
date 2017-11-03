from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^new/$', views.new),
	url(r'^create/$', views.create),
	url(r'^(?P<blog_id>\d)/$', views.display),
	url(r'^(?P<edit_id>\d)/edit/$', views.edit),
	url(r'^(?P<delete_id>\d)/delete/$', views.destroy)
]