from django.conf.urls import url

from .views import (
    NewApplicationView,
    PersonalInfoView,
)

urlpatterns = [

    url(r'^$', NewApplicationView.as_view(), name='new'),
    url(
        r'^(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/personal/$',
        PersonalInfoView.as_view(),
        name='step_2',
        kwargs={'step': 2},
    )

]
