from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SponsorSerializer, HackerSerializer


class SponsorsView(APIView):

    def post(self, request, format='json'):
        serializer = SponsorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        sponsor = serializer.save()
        if sponsor.pk:
            return Response({
                'status': 'ok',
                'message': 'Mail sent to sponsorships team.',
                'data': serializer.data
            })
        else:
            return Response({'status': 'error'})


class SupportView(APIView):

    def post(self, request, format='json'):
        serializer = HackerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        hacker = serializer.save()
        if hacker.pk:
            return Response({
                'status': 'ok',
                'message': 'Mail sent to support team.',
                'data': serializer.data
            })
        else:
            return Response({'status': 'error'})