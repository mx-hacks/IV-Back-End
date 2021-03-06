from django.conf.urls import url

from .views import (
    EducationView,
    EventsView,
    ExperienceView,
    FinishView,
    GoodiesView,
    HackathonsView,
    NewApplicationView,
    PersonalInfoView,
    PromoCodeView,
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
    ),

    url(
        r'^(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/goodies/$',
        GoodiesView.as_view(),
        name='goodies',
    ),

    url(
        r'^(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/experience/$',
        ExperienceView.as_view(),
        name='experience',
    ),

    url(
        r'^(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/hackathons/$',
        HackathonsView.as_view(),
        name='hackathons',
    ),

    url(
        r'^(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/events/$',
        EventsView.as_view(),
        name='events',
    ),

    url(
        r'^(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/finish/$',
        FinishView.as_view(),
        name='finish',
    ),

    url(
        r'^(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/promo_code/$',
        PromoCodeView.as_view(),
        name='promo_code',
    ),


]
