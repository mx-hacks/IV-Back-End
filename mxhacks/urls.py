from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from contact import urls as contact_urls

admin_url = r'^{}/'.format(settings.ADMIN_URL)

urlpatterns = [
    url(admin_url, include(admin.site.urls)),

    url(r'^contact/', include(contact_urls, namespace='contact')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # NOQA
