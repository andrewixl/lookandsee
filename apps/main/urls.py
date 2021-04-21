from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

urlpatterns = [
    url(r'^$', views.index),
    url(r'^about$', views.contact),
    url(r'^gethelp$', views.contact),
    url(r'^contact$', views.contact),
]