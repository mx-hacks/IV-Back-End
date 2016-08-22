from django.conf.urls import url

from .views import SponsorsView, SupportView

urlpatterns = [

    url(r'^sponsors/$', SponsorsView.as_view(), name='sponsors'),
    url(r'^support/$', SupportView.as_view(), name='support'),

]
