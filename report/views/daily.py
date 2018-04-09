from django.contrib import messages
from .. import models, forms
from .report import ReportUpdateView, ReportCreateView


class DailyReportView(ReportUpdateView):
    model = models.DailyReport
    template_name = "report/daily.html"
    form_class = forms.DailyReportForm
    event_types = [models.Event(title='Poop', color="#ff356e"), models.Event(title='Pee')]

    def get_context_data(self, **kwargs):
        context = super(DailyReportView, self).get_context_data()
        context['events'] = models.Report.objects.filter(organization=self.request.user.organization).all()
        context['event_types'] = self.event_types
        return context

    def form_valid(self, form):
        messages.success(self.request, "Daily report updated successfully")
        return super(DailyReportView, self).form_valid(form)


class DailyReportCreateView(ReportCreateView):
    model = models.DailyReport
    form_class = forms.DailyReportForm
