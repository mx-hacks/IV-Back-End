from rest_framework import serializers

from hackers.models import Hacker


class NewApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hacker
        fields = ('email',)