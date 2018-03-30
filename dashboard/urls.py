from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', login_required(views.DashboardView.as_view()), name='index'),
    path('administrators/', login_required(views.AdministratorListView.as_view()), name='administrators'),
    path('teachers/', login_required(views.TeacherListView.as_view()), name='teachers'),
    path('parents/', login_required(views.ParentListView.as_view()), name='parents'),
    path('students/', login_required(views.StudentListView.as_view()), name='students'),
]
