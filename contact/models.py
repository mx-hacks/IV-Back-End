from django.db import models


class Sponsor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=70)
    message = models.TextField(blank=True)

    # Metadata
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # Mailgun
    mail_sent = models.BooleanField(default=False)
    message_id = models.CharField(max_length=400)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        ordering = ('-created',)
