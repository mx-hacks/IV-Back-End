from django.shortcuts import get_object_or_404

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)
from rest_framework.response import Response

from .models import Campus, School

from .serializers import (
    CampusSerializer,
    SchoolSerializer,
)


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
                    'name': q.first().name,
                }
            }, status=400)

        return super(SchoolsView, self).create(request)


class CampusView(ListAPIView, CreateAPIView):
    
    serializer_class = CampusSerializer

    def get_queryset(self):
        return Campus.objects.filter(school=self.kwargs['pk'])

    def create(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        name = request.data.get('name', '')

        if len(name) < 2:
            return Response({
                'status': 'error',
                'message': 'El nombre debe contener al menos dos letras.'
            }, status=400)

        q = Campus.objects.filter(school=school, name=name)
        if q:
            return Response({
                'status': 'error',
                'message': 'Ya existe un campus con ese nombre.',
                'campus': {
                    'id': q.first().pk,
                    'school': q.first().school.pk,
                    'name': q.first().name,
                }
            }, status=400)

        campus = Campus(school=school, name=name)
        campus.save()
        serializer = CampusSerializer(campus)
        return Response(serializer.data, status=201)
