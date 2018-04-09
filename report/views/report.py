from django.views.generic import ListView, View, UpdateView
from django.shortcuts import redirect
from .. import models, forms
from django.http import JsonResponse
from core import models as core_models


class ReportCalendarView(ListView):
    template_name = 'report/calendar.html'
    model = models.Report

    def get_queryset(self):
        return super(ReportCalendarView, self).get_queryset().filter(user=self.kwargs['user_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ReportCalendarView, self).get_context_data(object_list=None, **kwargs)
        context['report_types'] = [models.Report(title='Daily')]
        return context


class ReportUpdateView(UpdateView):
    model = models.Report
    template_name = 'report/layout.html'
    form_class = forms.ReportForm


class JSONReportUpdateView(View):
    model = models.Report

    def post(self, request, pk):
        report = self.model.objects.get(pk=pk)
        for key in request.POST:
            setattr(report, key, request.POST[key])
        report.save()
        return JsonResponse({})


class ReportCreateView(View):

    def post(self, request, user_id):
        model = getattr(self, 'model', models.Report)
        report = model(organization=request.user.organization)
        for key in request.POST:
            setattr(report, key, request.POST[key])
        report.save()
        user = core_models.User.objects.get(pk=user_id)
        user.reports.add(report)
        return JsonResponse({'id': report.id})


class ReportDeleteView(View):
    def get(self, request, pk):
        report = models.Report.objects.get(pk=pk)
        user = core_models.User.objects.filter(reports=report).first()
        report.delete()
        return redirect('dashboard:report:calendar', user_id=user.id)
