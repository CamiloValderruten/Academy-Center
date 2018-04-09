from report import models as report_models
from django.shortcuts import reverse


class Attendance(report_models.Event):

    @property
    def url(self):
        return "/#"
