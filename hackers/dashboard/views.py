from django.views.generic import TemplateView

from mxhacks.mixins import AdminSession


class StatsView(AdminSession, TemplateView):
    
    template_name = 'dashboard/stats.html'
