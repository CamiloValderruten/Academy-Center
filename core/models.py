from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import RegexValidator
from django.shortcuts import reverse
from datetime import time


class Organization(models.Model):
    name = models.CharField(max_length=50, null=False, default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(upload_to='logos/', blank=True)

    day_start_time = models.TimeField(default=time(hour=7))
    day_end_time = models.TimeField(default=time(hour=18))

    on_trial = models.BooleanField(default=True)
    trial_started_on = models.DateTimeField(auto_now_add=True)
    stripe_client_id = models.CharField(max_length=100, default=None, null=True)

    def get_absolute_url(self):
        return reverse('core:organization', args=[str(self.id)])

    def __str__(self):
        return self.name


class OrganizationModel(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


class OrganizationAbstractUser(AbstractUser):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


class User(OrganizationAbstractUser):
    roles = ['administrator', 'teacher', 'parent', 'student']
    reports = models.ManyToManyField('report.Report')
    date_of_birth = models.DateField(null=True, blank=True, default=None)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    gender = models.CharField(max_length=15, choices=[('male', 'Male'), ('female', 'Female')], null=True, blank=True)

    attendance = models.ManyToManyField('attendance.Attendance')
    checked_in = models.BooleanField(default=False)

    @property
    def profile_image_url(self):
        male = "/static/images/boy.png"
        female = "/static/images/girl.png"
        return self.avatar.url if self.avatar else male if self.gender == "male" else female

    @property
    def role_level(self):
        """
        Gets the role of the user model, since it is not instantiated as a
        role model, then a query has to be made to find out which role this
        user belongs to, for this reason it is an expensive function.
        :return: Role of the user
        """
        user = Administrator.objects.filter(pk=self.pk).first()
        user = user if user else Teacher.objects.filter(pk=self.pk).first()
        user = user if user else Parent.objects.filter(pk=self.pk).first()
        user = user if user else Student.objects.filter(pk=self.pk).first()
        return user.role

    def get_or_create_group(self):
        role = getattr(self, 'role')
        group = Group.objects.filter(name=role).first()
        if not group:
            group = Group(name=role)
            group.save()
        return group

    def get_absolute_url(self):
        return reverse('dashboard:' + self.role_level, args=[str(self.id)])


class Administrator(User):
    role = 'administrator'

    def __init__(self, *args, **kwargs):
        super(Administrator, self).__init__(*args, **kwargs)
        group = self.get_or_create_group()
        self.save()
        self.groups.add(group)


class Teacher(User):
    role = 'teacher'

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        group = self.get_or_create_group()
        self.save()
        self.groups.add(group)


class Parent(User):
    role = 'parent'
    students = models.ManyToManyField("Student")
    send_email_reports = models.BooleanField(default=True)
    send_phone_reports = models.BooleanField(default=True)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        group = self.get_or_create_group()
        self.save()
        self.groups.add(group)


class Student(User):
    role = 'student'

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        group = self.get_or_create_group()
        self.save()
        self.groups.add(group)
