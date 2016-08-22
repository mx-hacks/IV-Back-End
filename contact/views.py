from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SponsorSerializer


class SponsorsView(APIView):

    def post(self, request, format='json'):
        serializer = SponsorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        sponsor = serializer.save()
        return Response({'status': 'ok'})
