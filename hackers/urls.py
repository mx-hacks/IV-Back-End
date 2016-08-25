from django.conf.urls import url

from .views import (
    CampusView,
    ELevelsView,
    EventsView,
    GoodiesView,
    HackathonsView,
    SchoolsView,
)

urlpatterns = [

    url(r'^schools/$', SchoolsView.as_view(), name='schools'),
    url(r'^schools/(?P<pk>\d+)/campus/$', CampusView.as_view(), name='campus'),
    url(r'^levels/$', ELevelsView.as_view(), name='levels'),
    url(r'^goodies/$', GoodiesView.as_view(), name='goodies'),
    url(r'^hackathons/$', HackathonsView.as_view(), name='hackathons'),
    url(r'^events/$', EventsView.as_view(), name='events'),

]
