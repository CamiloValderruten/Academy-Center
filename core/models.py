from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, Group
from django.core.validators import RegexValidator
from django.shortcuts import reverse
from django.conf.urls.static import static


class Organization(models.Model):
    name = models.CharField(max_length=50, null=False, default=None)
    created_on = models.DateTimeField(auto_now_add=True)

    on_trial = models.BooleanField(default=True)
    trial_started_on = models.DateTimeField(auto_now_add=True)
    stripe_client_id = models.CharField(max_length=100, default=None, null=True)


if Organization.objects.count() is 0:
    Organization(name="AcademyCenter").save()


class OrganizationUserManager(UserManager):
    def get_queryset(self):
        return super().get_queryset()

    def for_organization(self, organization):
        return self.get_queryset().filter(organization=organization)


class User(AbstractUser):
    roles = ['administrator', 'teacher', 'parent', 'student']
    objects = OrganizationUserManager()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    avatar = models.ImageField(default=None, blank=True)
    gender = models.CharField(max_length=15, choices=[('male', 'Male'), ('female', 'Female')], null=True, blank=True)

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
        group_filter = Group.objects.filter(name=role)
        group = Group(name=role) if group_filter.count() is 0 else group_filter.first()
        group.save()
        return group

    def get_absolute_url(self):
        return reverse('dashboard:' + self.role_level, args=[str(self.id)])


class Administrator(User):
    role = 'administrator'

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
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
