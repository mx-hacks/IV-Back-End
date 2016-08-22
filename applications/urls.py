from django.conf.urls import url

from .views import NewApplicationView

urlpatterns = [

    url(r'^$', NewApplicationView.as_view(), name='new'),

]
