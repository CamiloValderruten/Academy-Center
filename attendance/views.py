from django.views.generic import TemplateView, ListView
from django.shortcuts import redirect
from . import models
from core import models as core_models
from datetime import datetime


def index(request):
    return True


def check_in(request, user_id):
    user = core_models.User.objects.get(pk=user_id)
    if not user.checked_in:
        attendance = models.Attendance(organization=request.user.organization)
        attendance.save()
        user.attendance.add(attendance)
        user.checked_in = True
        user.save()
    return redirect(request.META.get('HTTP_REFERER'))


def check_out(request, user_id):
    user = core_models.User.objects.get(pk=user_id)
    if user.checked_in:
        attendance = user.attendance.filter(end=None).first()
        attendance.end = datetime.now()
        attendance.save()
        user.checked_in = False
        user.save()
    return redirect(request.META.get('HTTP_REFERER'))


class AttendanceCalendarView(ListView):
    template_name = 'attendance/calendar.html'
    model = models.Attendance

    def get_queryset(self):
        return super(AttendanceCalendarView, self).get_queryset().filter(user=self.kwargs['user_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AttendanceCalendarView, self).get_context_data(object_list=None, **kwargs)
        return context

