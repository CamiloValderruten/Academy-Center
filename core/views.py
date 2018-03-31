from . import models
from django.contrib import messages
from django.shortcuts import redirect


def delete_user(request, pk):
    user = models.User.objects.get(pk=pk, organization=request.user.organization)
    role = user.role_level
    user.delete()
    messages.success(request, 'User deleted successfully')
    return redirect('dashboard:' + role + "s")


def link_parent_student(request, parent_id, student_id):
    parent = models.Parent.objects.get(pk=parent_id, organization=request.user.organization)
    student = models.Student.objects.get(pk=student_id, organization=request.user.organization)
    parent.students.add(student)
    return redirect(request.META.get('HTTP_REFERER'))


def unlink_parent_student(request, parent_id, student_id):
    parent = models.Parent.objects.get(pk=parent_id, organization=request.user.organization)
    student = models.Student.objects.get(pk=student_id, organization=request.user.organization)
    parent.students.remove(student)
    return redirect(request.META.get('HTTP_REFERER'))
