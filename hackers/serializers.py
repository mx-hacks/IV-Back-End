from rest_framework import serializers

from .models import School


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        field = ('id', 'name')