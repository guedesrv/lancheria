# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from . import views

urlpatterns = [
    #url(r'^users/$', views.users_list, name='users_list'),
]