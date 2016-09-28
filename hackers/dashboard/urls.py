from django.conf.urls import url

from .views import StatsView

urlpatterns = [
    url(r'^$', StatsView.as_view(), name='stats'),
]
