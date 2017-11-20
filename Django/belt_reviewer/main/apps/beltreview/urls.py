from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
    url(r'^reviews$', views.review),
    url(r'^add$', views.add_book_review),
    url(r'^create$', views.create),
    url(r'^book/(?P<book_id>\d+)$', views.show_book),
    url(r'^book/(?P<book_id>\d+)/create$', views.create_add),
    url(r'^user/(?P<user_id>\d+)$', views.user),
]