from django.db import models
from django.core.validators import RegexValidator
from tenant_users.tenants.models import UserProfile


class User(UserProfile):
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=150, blank=True)
    date_of_birth = models.DateField(null=True, default=None)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    avatar = models.ImageField(default=None, blank=True)
    gender = models.CharField(max_length=15, choices=[('male', 'female')])


class Administrator(User):
    pass


class Teacher(User):
    pass


class Parent(User):
    students = models.ManyToManyField("Student")


class Student(User):
    pass

