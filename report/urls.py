from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'report'
urlpatterns = [
    path('<slug:pk>/event/create', login_required(views.EventCreateView.as_view()), name='event_create'),
    path('calendar/user/<user_id>', login_required(views.ReportCalendarView.as_view()), name='calendar'),
    path('<slug:pk>/update', login_required(views.JSONReportUpdateView.as_view()), name='update'),
    path('<slug:pk>/delete', login_required(views.ReportDeleteView.as_view()), name='delete'),

    path('daily/<slug:pk>', login_required(views.DailyReportView.as_view()), name='daily_report'),
    path('user/<user_id>/create/daily', login_required(views.DailyReportCreateView.as_view()), name='daily_create'),
]
