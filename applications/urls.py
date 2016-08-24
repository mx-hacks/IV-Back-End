from django.conf.urls import url

from .views import (
    EducationView,
    NewApplicationView,
    PersonalInfoView,
)

urlpatterns = [

    url(r'^$', NewApplicationView.as_view(), name='new'),
    url(
        r'^(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/personal/$',
        PersonalInfoView.as_view(),
        name='personal_info',
    ),

    url(
        r'^(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/education/$',
        EducationView.as_view(),
        name='education',
    )

]
