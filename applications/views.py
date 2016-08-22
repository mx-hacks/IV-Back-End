from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Application

from .serializers import (
    NewApplicationSerializer
)


class NewApplicationView(APIView):

    def post(self, request, format='json'):
        serializer = NewApplicationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        hacker = serializer.create(serializer.data)
        application = Application(
            hacker = hacker,
            step = 1
        )
        application.save()
        return Response({
            'status': 'ok',
            'message': 'New application in progress.',
            'step': application.step,
            'email': hacker.email
        })
