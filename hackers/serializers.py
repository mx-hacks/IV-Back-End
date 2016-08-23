from rest_framework import serializers

from .models import Campus, School


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        field = ('id', 'name')


class CampusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campus
        field = ('id', 'school', 'name')
