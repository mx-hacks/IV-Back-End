from rest_framework.response import Response
from rest_framework.views import APIView

from .mixins import HackerMixin
from .models import Application

from .serializers import (
    EdcuationSerializer,
    NewApplicationSerializer,
    PersonalInfoSerializer,
)


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
            'step': application.step,
            'email': hacker.email
        })


class PersonalInfoView(HackerMixin, APIView):

    def put(self, request, email, step, format='json'):
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
            'message': 'Personal info updated',
            'first_name': self.hacker.first_name,
            'last_name': self.hacker.last_name,
            'age': self.hacker.age,
            'male': self.hacker.male,
            'female': self.hacker.female,
            'phone_number': self.hacker.phone_number,
            'email': self.hacker.email,
        })


class EducationView(HackerMixin, APIView):

    def put(self, request, email, step, format='json'):
        serializer = EdcuationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
