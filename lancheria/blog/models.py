# -*- coding: utf-8 -*-
import os
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.conf import settings
from django.dispatch import receiver
from django.db import models
from django.db.models import permalink



class Post(models.Model):
  
    autor = models.ForeignKey('auth.User')  
    titulo = models.CharField('Título', max_length=255)
    slug = models.SlugField(max_length=100, unique=True)    
    texto = models.TextField()
    publicar = models.BooleanField(default=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.titulo

    @permalink
    def get_absolute_url(self):
        return ('view_noticias', None, { 'slug': self.slug })

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'  