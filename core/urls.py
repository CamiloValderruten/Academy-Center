from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('parent/<parent_id>/link/student/<student_id>', views.link_parent_student, name='link_parent_student'),
    path('parent/<parent_id>/unlink/student/<student_id>', views.unlink_parent_student, name='unlink_parent_student'),
]
