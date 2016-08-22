from django.conf import settings
from django.template.loader import render_to_string

from rest_framework import serializers

from .models import Sponsor, Hacker

from mxhacks.utils import send_mail


class SponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsor
        fields = (
            'first_name',
            'last_name',
            'email',
            'company',
            'message',
        )

    def create(self, data):
        message = render_to_string('contact/sponsors.html', data)

        mail = {
            'subject': '[MX Hacks Sponsorship] - {}'.format(data['company']),
            'from': 'MX Hacks Bot <bot@mxhacks.mx>',
            'to': [settings.SPONSORS_MAIL],
            'html': message
        }
        mailgun_data = send_mail(data=mail)

        if mailgun_data.status_code == 200:
            message_id = mailgun_data.json()['id']
            sponsor = Sponsor()
            sponsor.first_name = data['first_name']
            sponsor.last_name = data['last_name']
            sponsor.email = data['email']
            sponsor.company = data['company']
            sponsor.message = data.get('message', '')
            sponsor.sent = True
            sponsor.message_id = message_id
            sponsor.save()

            return sponsor

        else:
            return Sponsor()


class HackerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hacker
        fields = (
            'name',
            'email',
            'message',
        )

    def create(self, data):
        message = render_to_string('contact/support.html', data)

        mail = {
            'subject': '[Sporte MX Hacks] - {}'.format(data['name']),
            'from': '{name} <{email}>'.format(
                name=data['name'],
                email=data['email']
            ),
            'to': [settings.SUPPORT_MAIL],
            'html': message
        }
        mailgun_data = send_mail(data=mail)

        if mailgun_data.status_code == 200:
            message_id = mailgun_data.json()['id']
            hacker = Hacker()
            hacker.name = data['name']
            hacker.email = data['email']
            hacker.message = data['message']
            hacker.sent = True
            hacker.message_id = message_id
            hacker.save()
            return hacker

        else:
            return Hacker()
