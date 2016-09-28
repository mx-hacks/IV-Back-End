from django.shortcuts import get_object_or_404

from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Campus, School, EventEdition, Hackathon

from .serializers import (
    CampusSerializer,
    EventEditionSerializer,
    HackathonSerializer,
    SchoolSerializer,
)


class SchoolsView(CreateAPIView, ListAPIView):

    serializer_class = SchoolSerializer
    queryset = School.objects.all().order_by('name')
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

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
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

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


class ELevelsView(APIView):

    def get(self, request, format='json'):
        return Response([
            'Secundaria',
            'Preparatoria',
            'Bachillerato',
            'Universidad',
            'Maestría',
            'Doctorado',
        ])


class GoodiesView(APIView):

    def get(self, request, format='json'):
        return Response([
            'Chica - Mujer',
            'Mediana - Mujer',
            'Grande - Mujer',
            'Extra Grande - Mujer',
            'Chica - Hombre',
            'Mediana - Hombre',
            'Grande - Hombre',
            'Extra Grande - Hombre',
        ])


class EventsView(ListAPIView):
    serializer_class = EventEditionSerializer
    queryset = EventEdition.objects.all().order_by('name')


class HackathonsView(ListAPIView, CreateAPIView):
    serializer_class = HackathonSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    queryset = Hackathon.objects.all().order_by('name')

    def create(self, request):
        name = request.data.get('name', '')

        if len(name) < 2:
            return Response({
                'status': 'error',
                'message': 'El nombre debe contener al menos dos letras.'
            }, status=400)

        q = Hackathon.objects.filter(name=name)
        if q:
            return Response({
                'status': 'error',
                'message': 'Ya existe un hackathon con ese nombre.',
                'school': {
                    'id': q.first().pk,
                    'name': q.first().name,
                }
            }, status=400)

        return super(HackathonsView, self).create(request)
