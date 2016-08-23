from django.conf.urls import url

from .views import (
    CampusView,
    SchoolsView,
)

urlpatterns = [

    url(r'^schools/$', SchoolsView.as_view(), name='schools'),
    url(r'^schools/(?P<pk>\d+)/campus/$', CampusView.as_view(), name='campus'),

]
