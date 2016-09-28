from django.conf.urls import url

from .views import (
    
    # Analytics API
    ApplicationsPie,
    ApplicationsStat,
    DemographicsView,
    EducationStats,
    PunchCardView,

    # Export
    CSVView,
    ExportView,

    # Review
    ReviewApplications,

)

urlpatterns = [

    url(r'^export/$', ExportView.as_view(), name='export'),
    url(r'^export/(?P<pk>\d+)/$', CSVView.as_view(), name='csv'),

    url(r'^review/$', ReviewApplications.as_view(), name='review'),

    url(r'^api/stats/applications/$', ApplicationsStat.as_view(), name='applications_stats'),
    url(r'^api/stats/applications/pie/$', ApplicationsPie.as_view(), name='applications_pie'),
    url(r'^api/stats/education/$', EducationStats.as_view(), name='education_stats'),
    url(r'^api/stats/demographics/$', DemographicsView.as_view(), name='demographics_stats'),
    url(r'^api/stats/punchcard/$', PunchCardView.as_view(), name='punchcard'),
]
