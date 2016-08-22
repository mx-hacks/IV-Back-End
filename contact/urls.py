from django.conf.urls import url

from .views import SponsorsView

urlpatterns = [

    url(r'^sponsors/$', SponsorsView.as_view(), name='sponsors'),
    # url(r'^support/$', SupporView.as_view(), name='support'),

]
