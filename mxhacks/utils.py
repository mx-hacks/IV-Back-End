import requests

from mxhacks.settings.base import (
    MAILGUN_ENDPOINT,
    MAILGUN_API_KEY
)


def send_mail(data):
    data['o:tracking'] = 'yes'
    data['o:tracking-clicks '] = 'yes'
    data['o:tracking-opens'] = 'yes'
    response = requests.post(
        MAILGUN_ENDPOINT + 'messages',
        auth = ('api', MAILGUN_API_KEY),
        data = data
    )
    return response
