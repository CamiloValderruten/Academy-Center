from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'attendance'
urlpatterns = [
    path('', login_required(views.index), name='index'),
    path('user/<user_id>/check_in', login_required(views.check_in), name='check_in'),
    path('user/<user_id>/check_out', login_required(views.check_out), name='check_out'),
    path('user/<user_id>/calendar', login_required(views.AttendanceCalendarView.as_view()), name='calendar'),
]
