# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

#from .forms import ContactForm
#from .models import Contact



def index(request):
    return render(request, 'web/index.html') 