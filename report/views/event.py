from django.views.generic import FormView
from django.contrib import messages
from django.shortcuts import redirect
from .. import models, forms
from report import models as report_models


class EventCreateView(FormView):
    form_class = forms.EventForm
    http_method_names = ['post']
    template_name = 'report/layout.html'

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return super(EventCreateView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EventCreateView, self).get_context_data()
        return context

    def form_valid(self, form):
        report = report_models.Report.objects.get(pk=self.kwargs['pk'])
        event = report_models.Event(organization=self.request.user.organization, **form.cleaned_data)
        event.save()
        report.events.add(event)
        report.save()
        messages.success(self.request, "Event created successfully")
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        print(form.cleaned_data)
        messages.success(self.request, form.errors)
        return super(EventCreateView, self).form_invalid(form)
