from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from applications import urls as applications_urls
from applications.dashboard import urls as applications_dashboard_urls

from contact import urls as contact_urls

from hackers import urls as hackers_urls
from hackers.dashboard import urls as hackers_dashboard_urls

admin_url = r'^{}/'.format(settings.ADMIN_URL)
dashboard_url = r'^{}/'.format(settings.DASHBOARD_URL)

urlpatterns = [
    url(admin_url, include(admin.site.urls)),

    # API
    url(r'^contact/', include(contact_urls, namespace='contact')),
    url(r'^applications/', include(applications_urls, namespace='applications')),
    url(r'^hackers/', include(hackers_urls, namespace='hackers')),

    # Dashboard
    url(
        dashboard_url,
        include(hackers_dashboard_urls, namespace='hackers_dashboard') # NQOA
    ),

    url(
        dashboard_url,
        include(applications_dashboard_urls, namespace='applications_dashboard') # NQOA
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # NOQA
