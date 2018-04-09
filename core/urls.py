from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'core'
urlpatterns = [
    path('parent/<parent_id>/link/student/<student_id>', login_required(views.link_parent_student),
         name='link_parent_student'),
    path('parent/<parent_id>/unlink/student/<student_id>', login_required(views.unlink_parent_student),
         name='unlink_parent_student'),
    path('organization/<slug:pk>', login_required(views.OrganizationView.as_view()), name='organization')
]
