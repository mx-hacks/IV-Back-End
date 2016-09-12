from django.db import models

from hackers.models import Hacker


class Application(models.Model):

    hacker = models.OneToOneField(Hacker)
    accepted = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    step = models.IntegerField(default=0) # Current step (not finished)
    promo_code = models.CharField(max_length=50, blank=True)

    # Metadata
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hacker.email
