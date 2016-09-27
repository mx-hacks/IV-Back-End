from django.conf.urls import url

from .views import (
    ApplicationsPie,
    ApplicationsStat,
    DemographicsView,
    EducationStats,
    PunchCardView,
)

urlpatterns = [
    url(r'^api/stats/applications/$', ApplicationsStat.as_view(), name='applications_stats'),
    url(r'^api/stats/applications/pie/$', ApplicationsPie.as_view(), name='applications_pie'),
    url(r'^api/stats/education/$', EducationStats.as_view(), name='education_stats'),
    url(r'^api/stats/demographics/$', DemographicsView.as_view(), name='demographics_stats'),
    url(r'^api/stats/punchcard/$', PunchCardView.as_view(), name='punchcard'),
]
