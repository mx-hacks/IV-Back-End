from rest_framework.response import Response
from rest_framework.views import APIView

from .mixins import HackerMixin
from .models import Application

from .serializers import (
    EdcuationSerializer,
    ExperienceSerializer,
    GoodiesSerializer,
    NewApplicationSerializer,
    PersonalInfoSerializer,
)

from hackers.models import Campus, School, Hackathon, EventEdition
from hackers.serializers import HackerSerializer


class NewApplicationView(APIView):

    def post(self, request, format='json'):
        serializer = NewApplicationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        hacker = serializer.create(serializer.data)
        application = Application(
            hacker = hacker,
            step = 2
        )
        application.save()
        return Response({
            'status': 'ok',
            'message': 'New application in progress.',
            'hacker': HackerSerializer(hacker).data
        })


class PersonalInfoView(HackerMixin, APIView):

    def put(self, request, email, format='json'):
        serializer = PersonalInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        self.hacker.first_name = data['first_name']
        self.hacker.last_name = data['last_name']
        self.hacker.age = data['age']
        self.hacker.male = data['male']
        self.hacker.female = data['female']
        self.hacker.phone_number = data['phone_number']
        self.hacker.country = data['country']
        self.hacker.state = data['state']
        self.hacker.save()

        return Response({
            'status': 'ok',
            'message': 'Personal info updated.',
            'hacker': HackerSerializer(self.hacker).data
        })


class EducationView(HackerMixin, APIView):

    def put(self, request, email, format='json'):
        serializer = EdcuationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        self.hacker.school = School.objects.get(pk=data['school'])
        self.hacker.campus = Campus.objects.get(pk=data['campus'])
        self.hacker.school_join_year = data['school_join_year']
        self.hacker.school_graduation_year = data['school_graduation_year']
        self.hacker.school_identification = data['school_identification']
        self.hacker.education_level = data['education_level']
        self.hacker.major = data['major']
        self.hacker.save()

        self.hacker.application.step = 3
        self.hacker.application.save()

        return Response({
            'status': 'ok',
            'message': 'Education info updated.',
            'hacker': HackerSerializer(self.hacker).data
        })


class GoodiesView(HackerMixin, APIView):

    def put(self, request, email, format='json'):
        serializer = GoodiesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        self.hacker.tshirt_size = data['tshirt_size']
        self.hacker.dietary_restrictions = data.get('dietary_restrictions', '')
        self.hacker.save()

        self.hacker.application.step = 4
        self.hacker.application.save()

        return Response({
            'status': 'ok',
            'message': 'Goodies info updated.',
            'hacker': HackerSerializer(self.hacker).data
        })


class ExperienceView(HackerMixin, APIView):

    def put(self, request, email, format='json'):
        serializer = ExperienceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        self.hacker.first_time_hacker = data['first_time_hacker']
        self.hacker.currently_working = data['currently_working']
        self.hacker.save()

        return Response({
            'status': 'ok',
            'message': 'Experience info updated.',
            'hacker': HackerSerializer(self.hacker).data
        })


class HackathonsView(HackerMixin, APIView):

    def put(self, request, email, format='json'):
        hackathons = request.data.get('hackathons', None)
        if not hackathons:
            return Response({
                'status': 'error',
                'message': 'Missing hackathons data.'
            }, status=400)

        if type(hackathons) != list:
            return Response({
                'status': 'error',
                'message': 'A list of hackathons IDs is required.'
            }, status=400)

        hs = []
        for h in hackathons:
            try:
                hackathon = Hackathon.objects.get(pk=h)
            except:
                return Response({
                    'status': 'error',
                    'message': 'Hackathon {} does not exist.'.format(h)
                })
            hs.append(hackathon)

        self.hacker.hackathons.clear()
        self.hacker.save()
        self.hacker.hackathons.add(*hs)
        self.hacker.save()

        return Response({
            'status': 'ok',
            'message': 'Hackathons added to hacker experience.',
            'hacker': HackerSerializer(self.hacker).data
        })


class EventsView(HackerMixin, APIView):

    def post(self, request, email, format='json'):
        events = request.data.get('events', None)
        if not events:
            return Response({
                'status': 'error',
                'message': 'Missing events data.'
            }, status=400)

        events = [x for x in events.split(',') if type(x) == int]

        es = []
        for e in events:
            try:
                event = EventEdition.objects.get(pk=e)
            except:
                return Response({
                    'status': 'error',
                    'message': 'Event {} does not exist.'.format(e)
                })
            es.append(event)

        self.hacker.event_participations.clear()
        self.hacker.save()
        self.hacker.event_participations.add(*es)
        self.hacker.save()

        return Response({
            'status': 'ok',
            'message': 'Events added to hacker experience.',
            'hacker': HackerSerializer(self.hacker).data
        })


class FinishView(HackerMixin, APIView):

    def put(self, request, email, format='json'):
        self.hacker.application.finished = True
        self.hacker.application.step = 5
        self.hacker.application.save()

        return Response({
            'status': 'ok',
            'message': 'Application finished successfully!.',
            'hacker': HackerSerializer(self.hacker).data
        })