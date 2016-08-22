from django.conf import settings
from django.template.loader import render_to_string

from rest_framework import serializers

from .models import Sponsor

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
            return None
