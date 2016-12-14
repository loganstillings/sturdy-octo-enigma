from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^generated$', views.create),
    url(r'^reset$', views.reset)
]
