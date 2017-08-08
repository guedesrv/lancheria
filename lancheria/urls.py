# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    url(r'^', include('lancheria.web.urls', namespace='web')),  
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('lancheria.blog.urls', namespace='blog')),
    url(r'^payments/', include('lancheria.payments.urls', namespace='payments')),
    url(r'^cliente/', include('lancheria.accounts.urls', namespace='cliente'))
             
]

# Se Djando estiver em modo DEBUG, o django vai servir media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)