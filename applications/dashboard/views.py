from mxhacks.mixins import AdminSession

from rest_framework.response import Response
from rest_framework.views import APIView

from applications.models import Application


class ApplicationsStat(AdminSession, APIView):

    def get(self, request, format='json'):
        applications = Application.objects.all().order_by('created')
        daily_applications = []

        for application in applications:
            date_key = (
                str(application.created.year) + '-' +
                str(application.created.month) + '-' +
                "%02d" % application.created.day
            )

            day = None
            for application_day in daily_applications:
                if application_day['day'] == date_key:
                    day = application_day
                    break
            if not day:
                daily_applications.append({
                    'day': date_key,
                    'applications': 1
                })
            else:
                day['applications'] += 1

        return Response(daily_applications)
