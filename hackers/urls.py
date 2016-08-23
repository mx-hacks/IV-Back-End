from django.conf.urls import url

from .views import (
    SchoolsView,
)

urlpatterns = [

    url(r'^schools/$', SchoolsView.as_view(), name='schools'),

]
