from django.http import JsonResponse

from .models import Application

from hackers.models import Hacker


class HackerMixin(object):

    def dispatch(self, request, *args, **kwargs):
        email = kwargs.get('email', None)
        step = kwargs.get('step', None)

        try:
            hacker = Hacker.objects.get(email=email)
        except Hacker.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'Hacker does not exist.'
            }, status=400)

        try:
            application = hacker.application
        except Application.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'Application does not exist.'
            })

        if application:
            application = hacker.application
            if application.accepted or application.finished:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Application closed.'
                })

        self.hacker = hacker
        self.application = application
        return super(HackerMixin, self).dispatch(request, *args, **kwargs)