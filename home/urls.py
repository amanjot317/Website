
from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^pricing', views.pricing),
    url(r'^contact', views.contact),
    url(r'^signin', views.signin),
    url(r'^signup', views.signup),
    url(r'^subscribe', views.subscribe),

]
