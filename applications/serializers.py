from django.utils import timezone

from hackers.models import (
    Hacker,
    School,
    Campus,
)

from rest_framework import serializers

from datetime import timedelta


class NewApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hacker
        fields = ('email',)


class PersonalInfoSerializer(serializers.Serializer):

    first_name = serializers.CharField(
        max_length = 50,
        min_length = 2,
        trim_whitespace = True,
    )
    last_name = serializers.CharField(
        min_length = 2,
        max_length = 50,
        trim_whitespace = True,
    )

    age = serializers.IntegerField(
        min_value = 12,
        max_value = 80
    )

    male = serializers.BooleanField(default=False)
    female = serializers.BooleanField(default=False)

    phone_number = serializers.CharField(
        min_length = 8,
        max_length = 15,
    )

    def validate(self, data):
        if not any([data['male'], data['female']]):
            raise serializers.ValidationError('Wrong gender.')
        elif data['male'] and data['female']:
            raise serializers.ValidationError('Wrong gender.')
        return data


class EdcuationSerializer(serializers.Serializer):

    school = serializers.IntegerField(min_value=1)
    campus = serializers.IntegerField(min_value=1)
    school_identification = serializers.CharField(max_length=50)
    education_level =  serializers.CharField(max_length=20)
    major = serializers.CharField(max_length=80)
    school_join_year = serializers.IntegerField()
    school_graduation_year = serializers.IntegerField()

    def validate_school(self, school):
        try:
            school = School.objects.get(pk=school)
        except School.DoesNotExist:
            raise serializers.ValidationError('School does not exist.')
        return school.pk

    def validate_campus(self, campus):
        try:
            campus = Campus.objects.get(pk=campus)
        except Campus.DoesNotExist:
            raise serializers.ValidationError('Campus does not exits.')
        return campus.pk

    def validate_education_level(self, level):
        e_levels = [
            'Secundaria',
            'Preparatoria',
            'Bachillerato',
            'Maestría',
            'Doctorado',
        ]

        if level not in e_levels:
            raise serializers.ValidationError('Invalid education level.')
        return level

    def validate_school_graduation_year(self, year):
        if year < (timezone.now() - timedelta(days=365)).year:
            raise serializers.ValidationError('Graduation year ocurred a while ago :(') # NOQA
        return year

    def validate(self, data):
        school = School.objects.get(pk=data['school'])
        try:
            campus = Campus.objects.get(school=school, pk=data['campus'])
        except Campus.DoesNotExist:
            raise serializers.ValidationError(
                'Campus is not part of the selected school.'
            )
        return data
