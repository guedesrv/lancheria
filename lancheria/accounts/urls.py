# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from . import views

urlpatterns = [
    url(r'^add/$', views.add, name='add'),
]