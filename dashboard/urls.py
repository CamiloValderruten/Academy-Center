from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views
from core import views as core_views

app_name = 'dashboard'
urlpatterns = [
    path('', login_required(views.DashboardView.as_view()), name='index'),
    path('administrators/', login_required(views.AdministratorListView.as_view()), name='administrators'),
    path('teachers/', login_required(views.TeacherListView.as_view()), name='teachers'),
    path('parents/', login_required(views.ParentListView.as_view()), name='parents'),
    path('students/', login_required(views.StudentListView.as_view()), name='students'),
    path('administrator/create', login_required(views.AdministratorCreationView.as_view()),
         name='create_administrator'),
    path('teacher/create', login_required(views.TeacherCreationView.as_view()), name='create_teacher'),
    path('parent/create', login_required(views.ParentCreationView.as_view()), name='create_parent'),
    path('student/create', login_required(views.StudentCreationView.as_view()), name='create_student'),
    path('administrator/<slug:pk>', login_required(views.AdministratorView.as_view()), name='administrator'),
    path('teacher/<slug:pk>', login_required(views.TeacherView.as_view()), name='teacher'),
    path('parent/<slug:pk>', login_required(views.ParentView.as_view()), name='parent'),
    path('student/<slug:pk>', login_required(views.StudentView.as_view()), name='student'),
    path('users/<slug:pk>/delete', login_required(core_views.delete_user), name='delete_user'),
]
