from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

urlpatterns = [
    url(r'^$', views.index),
    url(r'^about$', views.about),
    url(r'^gethelp$', views.gethelp),
    url(r'^contact$', views.contact),
]
