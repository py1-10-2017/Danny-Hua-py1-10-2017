from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^show/(?P<course_id>\d+)$', views.show),
    url(r'^delete/(?P<course_id>\d+)$', views.delete)
]