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

from hackers.models import Campus, School
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
        self.hacker.save()

        return Response({
            'status': 'ok',
            'message': 'Experience info updated.',
            'hacker': HackerSerializer(self.hacker).data
        })
