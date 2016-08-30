from django.conf.urls import url

from .views import ApplicationsStat

urlpatterns = [
    url(r'^api/stats/applications/$', ApplicationsStat.as_view(), name='applications_stats'),
]
