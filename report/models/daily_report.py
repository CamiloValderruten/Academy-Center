from django.db import models
from django.shortcuts import reverse
from .report import Report


class DailyReport(Report):
    behavior = models.IntegerField(choices=[(0, 'Excellent'), (1, 'Cooperative'), (2, 'Uncooperative')], default=0)
    feeling = models.IntegerField(choices=[(0, 'Energetic'), (1, 'Happy'), (2, 'Active'), (3, 'Sad')], default=0)
    eat_amount = models.IntegerField(choices=[(0, 'All'), (1, 'Half'), (2, 'Little'), (3, 'None')], default=0)
    message = models.TextField(max_length=300, blank=True, )
    homework = models.TextField(max_length=300, blank=True)

    @property
    def url(self):
        return reverse('dashboard:report:daily_report', args=[str(self.id)])
