from rest_framework import serializers

from .models import Campus, Hacker, School, EventEdition, Hackathon


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ('id', 'name')


class CampusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campus
        fields = ('id', 'name')


class HackerSerializer(serializers.ModelSerializer):

    school = SchoolSerializer()
    campus = CampusSerializer()
    hackathons = serializers.StringRelatedField(many=True)
    event_participations = serializers.StringRelatedField(many=True)

    class Meta:
        model = Hacker
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'age',
            'male',
            'female',
            'country',
            'state',
            'phone_number',
            'school',
            'campus',
            'school_identification',
            'education_level',
            'major',
            'school_join_year',
            'school_graduation_year',
            'tshirt_size',
            'dietary_restrictions',
            'first_time_hacker',
            'hackathons',
            'event_participations',
            'first_time_event',
            'created',
            'modified',
        )


class HackathonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hackathon
        fields = ('id', 'name')


class EventEditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventEdition
        fields = ('id', 'name', 'edition')