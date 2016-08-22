from rest_framework import serializers

from hackers.models import Hacker


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
