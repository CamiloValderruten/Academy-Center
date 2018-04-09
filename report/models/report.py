from .event import Event
from django.db import models
from django.shortcuts import reverse


class Report(Event):
    events = models.ManyToManyField(Event, related_name='report_events')
