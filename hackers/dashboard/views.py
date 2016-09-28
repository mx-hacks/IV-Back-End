from django.views.generic import TemplateView

from mxhacks.mixins import StaffSession

from applications.models import Application


class StatsView(StaffSession, TemplateView):
    
    template_name = 'dashboard/stats.html'

    def get_context_data(self, **kwargs):
        context = super(StatsView, self).get_context_data(**kwargs)
        context['applications'] = {
            'total': Application.objects.all().count(),
            'finished': Application.objects.filter(finished=True).count(),
            'accepted': Application.objects.filter(accepted=True).count(),
        }
        return context
