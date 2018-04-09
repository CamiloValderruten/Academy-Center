from django.db import models
from django.shortcuts import reverse
from core import models as core_models
from datetime import datetime


class Event(core_models.OrganizationModel):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True)
    allDay = models.BooleanField(default=False)
    start = models.DateTimeField(null=False, default=datetime.utcnow)
    end = models.DateTimeField(null=True, default=None)
    color = models.CharField(max_length=10, default='#dd356e')
    textColor = models.CharField(max_length=10, default='white')

    @property
    def editable(self):
        return True

    @property
    def url(self):
        return reverse('dashboard:report:daily_report', args=[self.id])

    def get_absolute_url(self):
        return self.url
