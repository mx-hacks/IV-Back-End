from django.db import models
from django.contrib.auth.models import User

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


class Batch(models.Model):

    """Store applications exported batch."""

    created_by = models.ForeignKey(User)

    # Query arguments
    start_date = models.DateField()
    end_date = models.DateField()

    requested = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
