from django.forms import ModelForm, Textarea

from . import models


class EventForm(ModelForm):
    class Meta:
        model = models.Event
        fields = ('title', 'color', 'allDay', 'start', 'end')


class ReportForm(ModelForm):
    class Meta:
        model = models.Report
        exclude = ()


class DailyReportForm(ReportForm):
    class Meta:
        model = models.DailyReport
        fields = ('behavior', 'feeling', 'eat_amount', 'message', 'homework', )
        widgets = {
            'message': Textarea(attrs={'rows': 4, 'cols': 15}),
            'homework': Textarea(attrs={'rows': 4, 'cols': 15}),
        }
