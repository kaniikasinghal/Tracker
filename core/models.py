from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True)
    avatar_url = models.TextField(blank=True)

class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Employee(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    employee_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    date_of_joining = models.DateField()
    profile_picture_url = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    reporting_manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Project(models.Model):
    STATUS_CHOICES = [('active', 'Active'), ('on_hold', 'On Hold'), ('completed', 'Completed')]

    project_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='active')
    completion_percentage = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ProjectAssignment(models.Model):
    LOCK_CHOICES = [('hard', 'Hard'), ('soft', 'Soft')]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    lock_type = models.CharField(max_length=50, choices=LOCK_CHOICES, default='soft')
    utilization_percentage = models.IntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class HiringRequirement(models.Model):
    URGENCY_CHOICES = [('normal', 'Normal'), ('medium', 'Medium'), ('urgent', 'Urgent')]

    position_name = models.CharField(max_length=255)
    number_of_openings = models.IntegerField(default=1)
    urgency = models.CharField(max_length=50, choices=URGENCY_CHOICES, default='normal')
    experience_required = models.TextField()
    job_description = models.TextField(blank=True)
    job_document_url = models.TextField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)