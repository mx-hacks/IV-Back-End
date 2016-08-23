from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)
from rest_framework.response import Response

from .models import School
from .serializers import SchoolSerializer


class SchoolsView(CreateAPIView, ListAPIView):

    serializer_class = SchoolSerializer
    queryset = School.objects.all().order_by('name')

    def create(self, request):
        name = request.data.get('name', '')

        if len(name) < 2:
            return Response({
                'status': 'error',
                'message': 'El nombre debe contener al menos dos letras.'
            }, status=400)

        q = School.objects.filter(name=name)
        if q:
            return Response({
                'status': 'error',
                'message': 'Ya existe una escuela con ese nombre.',
                'school': {
                    'id': q.first().pk,
                    'nane': q.first().name,
                }
            })

        return super(SchoolsView, self).create(request)
