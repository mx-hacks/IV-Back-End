from django.conf.urls import url

from .views import (
    CampusView,
    ELevelsView,
    SchoolsView,
)

urlpatterns = [

    url(r'^schools/$', SchoolsView.as_view(), name='schools'),
    url(r'^schools/(?P<pk>\d+)/campus/$', CampusView.as_view(), name='campus'),
    url(r'^levels/$', ELevelsView.as_view(), name='levels'),

]
